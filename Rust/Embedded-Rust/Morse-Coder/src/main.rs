#![no_std]
#![no_main]

use core::str;

use cyw43::{Control, aligned_bytes};
use cyw43_pio::{DEFAULT_CLOCK_DIVIDER, PioSpi};
use defmt::{panic, unwrap};
use embassy_executor::Spawner;
use embassy_rp::gpio::{Level, Output};
use embassy_rp::peripherals::{DMA_CH0, PIO0, USB};
use embassy_rp::pio::{InterruptHandler, Pio};
use embassy_rp::usb::{Driver, Instance, InterruptHandler as UsbInterruptHandler};
use embassy_rp::{bind_interrupts, dma};
use embassy_time::Timer;
use embassy_usb::UsbDevice;
use embassy_usb::class::cdc_acm::{CdcAcmClass, State};
use embassy_usb::driver::EndpointError;
use static_cell::StaticCell;
use {defmt_rtt as _, panic_probe as _};

//* ------------- */
//* --- SETUP --- */
//* ------------- */
// Tells interrupts which handler function to call
bind_interrupts!(struct Irqs {
    PIO0_IRQ_0 => InterruptHandler<PIO0>;
    DMA_IRQ_0 => dma::InterruptHandler<DMA_CH0>;
    USBCTRL_IRQ => UsbInterruptHandler<USB>;
});

// Wifi chip has to run forever
// Used for blinking the LED
#[embassy_executor::task]
async fn cyw43_task(runner: cyw43::Runner<'static, cyw43::SpiBus<Output<'static>, PioSpi<'static, PIO0, 0>>>) -> ! {
    runner.run().await
}


//* ---------------------- */
//* ------ USB UART ------ */
//* ---------------------- */
type MyUsbDriver = Driver<'static, USB>;
type MyUsbDevice = UsbDevice<'static, MyUsbDriver>;

// USB driver has the run forever
#[embassy_executor::task]
async fn usb_task(mut usb: MyUsbDevice) -> ! {
    usb.run().await
}

struct Disconnected {}

impl From<EndpointError> for Disconnected {
    fn from(val: EndpointError) -> Self {
        match val {
            EndpointError::BufferOverflow => panic!("Buffer overflow"),
            EndpointError::Disabled => Disconnected {},
        }
    }
}





//* --------------------- */
//* ------ MY CODE ------ */
//* --------------------- */

async fn output_morse_code<'d, T: Instance + 'd>(cdc_acm: &mut CdcAcmClass<'d, Driver<'d, T>>, cyw43_control: &mut Control<'_>, str: &str) -> Result<(), Disconnected> {
    for &symbol in str.as_bytes() {
        cdc_acm.write_packet(&[symbol]).await?;
        cyw43_control.gpio_set(0, true).await;
        match symbol {
            b'-' => {
                Timer::after_millis(300).await;
            }
            b'.' => {
                Timer::after_millis(100).await;
            }
            _ => {}
        }
        cyw43_control.gpio_set(0, false).await;
        Timer::after_millis(100).await;
    }
    Ok(())
}

// Handle input/output using the usb serial connection
async fn handle_usb_serial_connection<'d, T: Instance + 'd>(cdc_acm: &mut CdcAcmClass<'d, Driver<'d, T>>, cyw43_control: &mut Control<'_>) -> Result<(), Disconnected> {
    let mut input_buffer = [0u8; 256];
    let mut input_len = 0;
    let mut buffer = [0u8; 128];
    loop {
        // Load input into line_buffer until enter is pressed
        let packet_length = cdc_acm.read_packet(&mut buffer).await?;

        for &packet_byte in &buffer[..packet_length] {
            match packet_byte {
                b'\r' => { // If "enter" is recieved
                    cdc_acm.write_packet(b"\r\n").await?;

                    // Output the line in morse code
                    for &byte in &input_buffer[..input_len] {
                        let byte = byte.to_ascii_uppercase();

                        match byte {
                            b'A'..=b'Z' | b'a'..=b'z' => { // Any letter, uppercase or lowercase
                                cdc_acm.write_packet(&[byte, b' ', b'>', b' ']).await?;
                                output_morse_code(cdc_acm, cyw43_control, MORSE_LETTERS[(byte - b'A') as usize]).await?;
                                Timer::after_millis(500).await;
                            }
                            b'0'..=b'9' => {
                                cdc_acm.write_packet(&[byte]).await?;
                                output_morse_code(cdc_acm, cyw43_control, MORSE_NUMBERS[(byte - b'0') as usize]).await?;
                                Timer::after_millis(500).await;
                            }
                            b' ' => {
                                Timer::after_millis(700).await;
                            }
                            _ => {}
                        }

                        cdc_acm.write_packet(b"\r\n").await?;
                    }

                    input_len = 0;
                }

                b'\x7f' => {
                    if input_len > 0 {
                        input_len -= 1;
                    }
                    cdc_acm.write_packet(&[packet_byte]).await?;
                }
                _ => {
                    cdc_acm.write_packet(&[packet_byte]).await?;
                    if input_len < input_buffer.len() {
                        input_buffer[input_len] = packet_byte;
                        input_len += 1;
                    }
                }
            }
        }
    }
}

const MORSE_NUMBERS: [&str; 10] = [
    "-----", // 0
    ".----", // 1
    "..---", // 2
    "...--", // 3
    "....-", // 4
    ".....", // 5
    "-....", // 6
    "--...", // 7
    "---..", // 8
    "----.", // 9
];

const MORSE_LETTERS: [&str; 26] = [
    ".-",   // A
    "-...", // B
    "-.-.", // C
    "-..",  // D
    ".",    // E
    "..-.", // F
    "--.",  // G
    "....", // H
    "..",   // I
    ".---", // J
    "-.-",  // K
    ".-..", // L
    "--",   // M
    "-.",   // N
    "---",  // O
    ".--.", // P
    "--.-", // Q
    ".-.",  // R
    "...",  // S
    "-",    // T
    "..-",  // U
    "...-", // V
    ".--",  // W
    "-..-", // X
    "-.--", // Y
    "--..", // Z
];


//* ------------------ */
//* ------ MAIN ------ */
//* ------------------ */
#[embassy_executor::main]
async fn main(spawner: Spawner) {
    // Variable initialisation
    let p = embassy_rp::init(Default::default());
    

    //* ----------------------- */
    //* --- BLINK LED SETUP --- */
    //* ----------------------- */
    // Needed for cyw43 wifi chip set up
    let fw = aligned_bytes!("../cyw43-firmware/43439A0.bin");
    let clm = aligned_bytes!("../cyw43-firmware/43439A0_clm.bin");
    let nvram = aligned_bytes!("../cyw43-firmware/nvram_rp2040.bin");
    let pwr = Output::new(p.PIN_23, Level::Low);
    let cs = Output::new(p.PIN_25, Level::High);
    let mut pio = Pio::new(p.PIO0, Irqs);
    let spi = PioSpi::new(
        &mut pio.common,
        pio.sm0,
        DEFAULT_CLOCK_DIVIDER,
        pio.irq0,
        cs,
        p.PIN_24,
        p.PIN_29,
        dma::Channel::new(p.DMA_CH0, Irqs),
    );

    // Set up cyw43 wifi chip
    static STATE: StaticCell<cyw43::State> = StaticCell::new();
    let state = STATE.init(cyw43::State::new());
    let (_net_device, mut cyw43_control, runner) = cyw43::new(state, pwr, spi, fw, nvram).await;
    spawner.spawn(unwrap!(cyw43_task(runner)));

    // control is how we blink the LED
    cyw43_control.init(clm).await;
    cyw43_control
        .set_power_management(cyw43::PowerManagementMode::PowerSave)
        .await;


    //* ---------------------- */
    //* ------ USB UART ------ */
    //* ---------------------- */
    // Create the driver, from the HAL.
    let usb_driver = Driver::new(p.USB, Irqs);

    // Create embassy-usb Config
    let config = {
        let mut config = embassy_usb::Config::new(0xc0de, 0xcafe);
        config.manufacturer = Some("Embassy");
        config.product = Some("USB-serial example");
        config.serial_number = Some("12345678");
        config.max_power = 100;
        config.max_packet_size_0 = 64;
        config
    };

    // Create embassy-usb DeviceBuilder using the driver and config.
    // It needs some buffers for building the descriptors.
    let mut builder = {
        static CONFIG_DESCRIPTOR: StaticCell<[u8; 256]> = StaticCell::new();
        static BOS_DESCRIPTOR: StaticCell<[u8; 256]> = StaticCell::new();
        static CONTROL_BUF: StaticCell<[u8; 64]> = StaticCell::new();

        let builder = embassy_usb::Builder::new(
            usb_driver,
            config,
            CONFIG_DESCRIPTOR.init([0; 256]),
            BOS_DESCRIPTOR.init([0; 256]),
            &mut [], // no msos descriptors
            CONTROL_BUF.init([0; 64]),
        );
        builder
    };

    // Create classes on the builder.
    let mut cdc_acm = {
        static STATE: StaticCell<State> = StaticCell::new();
        let state = STATE.init(State::new());
        CdcAcmClass::new(&mut builder, state, 64)
    };

    // Build the builder.
    let usb = builder.build();

    // Run the USB device.
    spawner.spawn(unwrap!(usb_task(usb)));

    // Do stuff with the usb serial connection
    loop {
        cdc_acm.wait_connection().await;
        let _ = handle_usb_serial_connection(&mut cdc_acm, &mut cyw43_control).await;
    }
}