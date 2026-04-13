This is a simple embedded rust program for the Raspberry PI Pico 2040 W.

It taks input from usb serial connection (basically USB UART), at any buad rate, and will show you the morse code of your input.

Easily flash to Pico using `cargo run --release` with the Pico plugged in holding the `BOOTSEL` button, to put it into flash mode.