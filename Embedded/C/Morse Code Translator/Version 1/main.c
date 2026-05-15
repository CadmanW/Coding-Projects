#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/pwm.h"


// -----------------------
// Hardware configuration
// -----------------------

// GPIO pins
#define LED_GPIO_PIN 1
#define PIEZO_BUZZER_GPIO_PIN  0

// PWM wrap value - with the clock divider below this sets the tone frequency
// of the square wave fed into the piezo buzzer.
#define PWM_WRAP 2600
// PWM duty cycle: 1-99% of PWM_WRAP. Controls perceived volume on the buzzer;
// 50% is the loudest for a symmetric square wave.
#define PWM_DUTY_CYCLE (PWM_WRAP * 0.50)


// ---------------------------------------------------------------------------
// Morse timing
// ---------------------------------------------------------------------------

// The base time unit of Morse code. Every other duration is a multiple of this.
// Decrease for faster keying, increase for slower / easier-to-read output.
#define MORSE_UNIT_MS 100

// Mark (key-down) durations
#define DOT_TIME_MS   (MORSE_UNIT_MS * 1)
#define DASH_TIME_MS  (MORSE_UNIT_MS * 3)

// Space (key-up) durations
#define SYMBOL_SPACING_MS  (MORSE_UNIT_MS * 1)  // between dots/dashes in a letter
#define LETTER_SPACING_MS  (MORSE_UNIT_MS * 3)  // between letters in a word
#define WORD_SPACING_MS    (MORSE_UNIT_MS * 7)  // between words


// ---------------------------------------------------------------------------
// Lookup tables
// ---------------------------------------------------------------------------

// Maps an ASCII character to its Morse code string
static const char* morseTable[] = {
    /* Numbers */
    ['0']  = "-----",
    ['1']  = ".----",
    ['2']  = "..---",
    ['3']  = "...--",
    ['4']  = "....-",
    ['5']  = ".....",
    ['6']  = "-....",
    ['7']  = "--...",
    ['8']  = "---..",
    ['9']  = "----.",

    /* Uppercase letters */
    ['A']  = ".-",
    ['B']  = "-...",
    ['C']  = "-.-.",
    ['D']  = "-..",
    ['E']  = ".",
    ['F']  = "..-.",
    ['G']  = "--.",
    ['H']  = "....",
    ['I']  = "..",
    ['J']  = ".---",
    ['K']  = "-.-",
    ['L']  = ".-..",
    ['M']  = "--",
    ['N']  = "-.",
    ['O']  = "---",
    ['P']  = ".--.",
    ['Q']  = "--.-",
    ['R']  = ".-.",
    ['S']  = "...",
    ['T']  = "-",
    ['U']  = "..-",
    ['V']  = "...-",
    ['W']  = ".--",
    ['X']  = "-..-",
    ['Y']  = "-.--",
    ['Z']  = "--..",

    /* Lowercase letters (same patterns as uppercase) */
    ['a']  = ".-",
    ['b']  = "-...",
    ['c']  = "-.-.",
    ['d']  = "-..",
    ['e']  = ".",
    ['f']  = "..-.",
    ['g']  = "--.",
    ['h']  = "....",
    ['i']  = "..",
    ['j']  = ".---",
    ['k']  = "-.-",
    ['l']  = ".-..",
    ['m']  = "--",
    ['n']  = "-.",
    ['o']  = "---",
    ['p']  = ".--.",
    ['q']  = "--.-",
    ['r']  = ".-.",
    ['s']  = "...",
    ['t']  = "-",
    ['u']  = "..-",
    ['v']  = "...-",
    ['w']  = ".--",
    ['x']  = "-..-",
    ['y']  = "-.--",
    ['z']  = "--.."
};

// Maps a Morse symbol ('.' or '-') to its on-air duration in milliseconds.
static const int morseSpacing[] = {
    ['-'] = DASH_TIME_MS,
    ['.'] = DOT_TIME_MS
};


// ---------------------------------------------------------------------------
// Peripheral setup
// ---------------------------------------------------------------------------

// Configures the LED GPIO as a digital output.
void init_led(void)
{
    gpio_set_function(LED_GPIO_PIN, GPIO_FUNC_SIO);
    gpio_set_dir(LED_GPIO_PIN, GPIO_OUT);
    gpio_put(LED_GPIO_PIN, 0);
}

// Configures the PWM slice that drives the piezo buzzer GPIO and returns the
// slice number so the caller can later enable/disable the tone.
//
// The clock divider + PWM_WRAP together pick the audio frequency:
//     f = 125 MHz / clkdiv / (PWM_WRAP + 1)
//       = 125e6 / 125 / 2601  ~= 384 Hz
uint init_piezo_buzzer(void)
{
    gpio_set_function(PIEZO_BUZZER_GPIO_PIN, GPIO_FUNC_PWM);

    uint sliceNum = pwm_gpio_to_slice_num(PIEZO_BUZZER_GPIO_PIN);

    pwm_set_clkdiv(sliceNum, 125.f);
    pwm_set_wrap(sliceNum, PWM_WRAP);
    pwm_set_chan_level(sliceNum, PWM_CHAN_A, PWM_DUTY_CYCLE);

    // PWM stays disabled here -- output_morse() toggles it per dot/dash.
    return sliceNum;
}


// ---------------------------------------------------------------------------
// Output helpers
// ---------------------------------------------------------------------------

// Drives the LED on (true) or off (false).
void led_on(bool on)
{
    gpio_put(LED_GPIO_PIN, on);
}

// Plays a single character as Morse code:
//   - alphanumerics      -> blink LED + sound buzzer for each dot/dash
//   - space (' ')        -> a word-length silence
//   - any other char     -> ignored
//
// Also prints "<c> = <pattern>" to stdout so the operator can follow along
// over the serial terminal.
//
// piezoSliceNum is the PWM slice returned from init_piezo_buzzer().
void output_morse(char c, uint piezoSliceNum)
{
    printf("%c = ", c);

    // Gap between this letter and whatever came before it.
    sleep_ms(LETTER_SPACING_MS);

    const char* morse = morseTable[(unsigned char)c];

    if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9'))
    {
        for (size_t i = 0; morse[i] != '\0'; i++)
        {
            const char symbol = morse[i];

            // Key down: LED on + buzzer on for the mark duration.
            led_on(true);
            pwm_set_enabled(piezoSliceNum, true);
            printf("%c", symbol);
            sleep_ms(morseSpacing[symbol]);

            // Key up: short gap before the next dot/dash in this letter.
            led_on(false);
            pwm_set_enabled(piezoSliceNum, false);
            sleep_ms(SYMBOL_SPACING_MS);
        }
    }
    else if (c == ' ')
    {
        sleep_ms(WORD_SPACING_MS);
    }
}


// ---------------------------------------------------------------------------
// Entry point
// ---------------------------------------------------------------------------

int main(void)
{
    // Bring up peripherals.
    stdio_init_all(); // USB serial
    init_led(); // LED
    uint piezoSliceNum = init_piezo_buzzer(); // Piezo Buzzer

    // Line buffer for the currently-typed message.
    char buffer[64];
    size_t bufferIndex = 0;

    while (true)
    {
        // Non-blocking read - returns PICO_ERROR_TIMEOUT when no key is ready.
        int c = stdio_getchar_timeout_us(0);
        switch (c)
        {
            case PICO_ERROR_TIMEOUT:
                // Nothing typed this tick; keep polling.
                break;

            case '\r':
                // ENTER pressed - play back the buffered line as Morse.
                printf("\r\n");
                for (size_t i = 0; i < bufferIndex; i++)
                {
                    output_morse(buffer[i], piezoSliceNum);
                    printf("\n");
                }
                bufferIndex = 0;
                break;

            default:
                // Echo so the user can see what they're typing in PuTTY,
                // then append to the line buffer if there's still room.
                printf("%c", c);
                if (bufferIndex < sizeof(buffer))
                {
                    buffer[bufferIndex++] = (char)c;
                }
                break;
        }
    }
}
