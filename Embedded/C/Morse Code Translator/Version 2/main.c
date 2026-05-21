#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/pwm.h"


// -----------------------
// Hardware configuration
// -----------------------

// GPIO pins
#define BUTTON_GPIO_PIN 3
#define PIEZO_BUZZER_GPIO_PIN 4
#define LED_GPIO_PIN 2

// PWM wrap value - with the clock divider below this sets the tone frequency
// of the square wave fed into the piezo buzzer.
#define PWM_WRAP 2600
// PWM duty cycle: 1-99% of PWM_WRAP. Controls perceived volume on the buzzer;
// 50% is the loudest for a symmetric square wave.
#define PWM_DUTY_CYCLE (PWM_WRAP * 0.50)

// ---------------------------------------------------------------------------
// Morse Code
// ---------------------------------------------------------------------------

// The base time unit of Morse code. Every other duration is a multiple of this.
// Decrease for faster keying, increase for slower / easier-to-read output.
#define MORSE_UNIT_MS 200

// Mark (key-down) durations
#define DOT_TIME_MS   (MORSE_UNIT_MS * 1)
#define DASH_TIME_MS  (MORSE_UNIT_MS * 3)

// Space (key-up) durations
#define SYMBOL_SPACING_MS  (MORSE_UNIT_MS * 1)  // between dots/dashes in a letter
#define LETTER_SPACING_MS  (MORSE_UNIT_MS * 3)  // between letters in a word
#define WORD_SPACING_MS    (MORSE_UNIT_MS * 7)  // between words

// I'm using a Trie for finding which character the morse code represents.
// This will be represented in the form of a 2d array.
// . = 2i+1
// - = 2i+2
static const char MORSE_TRIE[] = {
    '\0', // [0]  root         
    'E',  // [1]  .            
    'T',  // [2]  -            
    'I',  // [3]  ..           
    'A',  // [4]  .-           
    'N',  // [5]  -.           
    'M',  // [6]  --           
    'S',  // [7]  ...          
    'U',  // [8]  ..-          
    'R',  // [9]  .-.          
    'W',  // [10] .--          
    'D',  // [11] -..          
    'K',  // [12] -.-          
    'G',  // [13] --.          
    'O',  // [14] ---          
    'H',  // [15] ....         
    'V',  // [16] ...-         
    'F',  // [17] ..-.         
    '\0', // [18] ..-  (unused)
    'L',  // [19] .-..         
    '\0', // [20] .-.- (unused)
    'P',  // [21] .--.         
    'J',  // [22] .---         
    'B',  // [23] -...         
    'X',  // [24] -..-         
    'C',  // [25] -.-.         
    'Y',  // [26] -.--         
    'Z',  // [27] --..         
    'Q',  // [28] --.-         
    '\0', // [29] ---. (unused)
    '\0', // [30] ---- (unused)
};


// --------
// Setup
// --------

uint init_peripherals()
{
    // Button
    gpio_set_function(BUTTON_GPIO_PIN, GPIO_FUNC_SIO);
    gpio_set_dir(BUTTON_GPIO_PIN, GPIO_IN);
    gpio_pull_up(BUTTON_GPIO_PIN);

    // LED
    gpio_set_function(LED_GPIO_PIN, GPIO_FUNC_SIO);
    gpio_set_dir(LED_GPIO_PIN, GPIO_OUT);
    gpio_put(LED_GPIO_PIN, false);

    // Piezo Buzzer
    gpio_set_function(PIEZO_BUZZER_GPIO_PIN, GPIO_FUNC_PWM);
    uint slice_num = pwm_gpio_to_slice_num(PIEZO_BUZZER_GPIO_PIN);
    pwm_set_clkdiv(slice_num, 125.f);
    pwm_set_wrap(slice_num, PWM_WRAP);
    pwm_set_chan_level(slice_num, PWM_CHAN_A, PWM_DUTY_CYCLE);
    
    // Return the PWM slice that controls the piezo buzzer, to be used for toggling it on and off
    return slice_num;
}


// -----------------
// Helper Functions
// -----------------

// Uses the piezo buzzer and LED to output some sample morse code:
// 3 dots, 3 dashes, then 1 dot; so user can see the timings. (This helped me learn the timings for this project)
void output_example_morse_timings(int piezo_slice_num)
{
    // 3 dots
    for (uint8_t i = 0; i < 3; i++)
    {
        pwm_set_enabled(piezo_slice_num, true);
        gpio_put(LED_GPIO_PIN, true);
        sleep_ms(DOT_TIME_MS);

        pwm_set_enabled(piezo_slice_num, false);
        gpio_put(LED_GPIO_PIN, false);
        sleep_ms(SYMBOL_SPACING_MS);
    }

    sleep_ms(LETTER_SPACING_MS);

    // 3 dashes
    for (uint8_t i = 0; i < 3; i++)
    {
        pwm_set_enabled(piezo_slice_num, true);
        gpio_put(LED_GPIO_PIN, true);
        sleep_ms(DASH_TIME_MS);

        pwm_set_enabled(piezo_slice_num, false);
        gpio_put(LED_GPIO_PIN, false);
        sleep_ms(SYMBOL_SPACING_MS);
    }

    sleep_ms(WORD_SPACING_MS);

    // 1 dot
    pwm_set_enabled(piezo_slice_num, true);
    gpio_put(LED_GPIO_PIN, true);
    sleep_ms(DOT_TIME_MS);

    pwm_set_enabled(piezo_slice_num, false);
    gpio_put(LED_GPIO_PIN, false);

}

// Approximates the morse symbol from an amount of time in milliseconds
// the if statement is checking if ms is less than
// Half of the difference of the DASH_TIME and the DOT_TIME
char approximate_morse_symbol_from_ms(uint32_t ms)
{
    if (ms < DOT_TIME_MS + ((DASH_TIME_MS - DOT_TIME_MS) / 2))
        return '.';
    else
        return '-';
}

// Approximates the spacing between symbols for an amount of time in milliseconds
// Uses same kinda the same formula as approximate_morse_symbol_from_ms for bounds
char approximate_morse_spacing_from_ms(uint32_t ms)
{
    if (ms < SYMBOL_SPACING_MS + ((LETTER_SPACING_MS - SYMBOL_SPACING_MS) / 2))
        return '\0';
    else if (ms < LETTER_SPACING_MS + ((WORD_SPACING_MS - LETTER_SPACING_MS) / 2))
        return ' ';
    else
        return '\n';
}

// Traverses the trie until stopping at the correct node
// More information on this in README.md
char morse_to_char(const char morse_str[])
{
    int i = 0;
    while (*morse_str)
    {
        if (*morse_str == '.')
            i = 2 * i + 1;
        else if (*morse_str == '-')
            i = 2 * i + 2;
        
        morse_str++;
    }

    return MORSE_TRIE[i];
}




// ------------
// Entry Point
// ------------

int main(void)
{
    stdio_init_all();
    uint piezo_slice_num = init_peripherals();

    bool first_button_press = true;
    bool button_held = false;
    bool button_pressed = false;
    uint32_t button_pressed_time_ms = 0;
    uint32_t button_released_time_ms = 0;
    uint32_t button_held_duration_ms = 0;
    uint32_t button_not_held_duration_ms = 0;
    char morse_symbol = '\0';
    char morse_symbol_buffer[255];
    uint8_t morse_symbol_buffer_index = 0;
    char ascii_buffer[255];
    uint8_t ascii_buffer_index = 0;

    output_example_morse_timings(piezo_slice_num);

    while (true)
    {
        button_held = !gpio_get(BUTTON_GPIO_PIN);

        if (button_held && !button_pressed)
        { // Button Pressed

            // Enable LED and Piezo Buzzer
            pwm_set_enabled(piezo_slice_num, true);
            gpio_put(LED_GPIO_PIN, true);

            // Save time
            button_pressed_time_ms = time_us_32() / 1000;
            button_pressed = true;

            // Skip the first button press
            if (!first_button_press)
            {
                // Do stuff with the updated button pressed time
                if (button_not_held_duration_ms = button_pressed_time_ms - button_released_time_ms)
                {
                    char morse_spacing = approximate_morse_spacing_from_ms(button_not_held_duration_ms);
                    if (morse_spacing == ' ')
                    {
                        // Null terminate morse_str_buffer[]
                        morse_symbol_buffer[morse_symbol_buffer_index] = '\0';
                        // Append morse_symbol_buffer's morse --> char to ascii_buffer
                        ascii_buffer[ascii_buffer_index++] = morse_to_char(morse_symbol_buffer);
                        // Clear morse_str_buffer
                        morse_symbol_buffer_index = 0;
                    }
                    else if (morse_spacing == '\n')
                    {
                        // Null terminate morse_str_buffer[]
                        morse_symbol_buffer[morse_symbol_buffer_index] = '\0';
                        char c = morse_to_char(morse_symbol_buffer);
                        if (c)
                        {
                            ascii_buffer[ascii_buffer_index++] = c;
                            morse_symbol_buffer_index = 0;
                            // add a space to the final ascii str
                            ascii_buffer[ascii_buffer_index++] = ' ';
                        }
                    }

                    // Output the translated morse code
                    morse_symbol_buffer[morse_symbol_buffer_index] = '\0';  // null terminate
                    ascii_buffer[ascii_buffer_index] = '\0'; // null terminate
                    printf("\033[2J\033[H");  // clear screen

                    printf("%s\n", ascii_buffer); // Output the ascii buffer
                    printf("%s", morse_symbol_buffer); // Output the morse buffer
                }
            }
            first_button_press = false;
        } 
        else if (!button_held && button_pressed)
        { // Button Released
            // Disable LED and Piezo Buzzer
            pwm_set_enabled(piezo_slice_num, false);
            gpio_put(LED_GPIO_PIN, false);

            // Save time
            button_released_time_ms = time_us_32() / 1000;
            button_pressed = false;

            // Do stuff with the updated button released time
            if (button_held_duration_ms = button_released_time_ms - button_pressed_time_ms)
            {
                morse_symbol_buffer[morse_symbol_buffer_index++] = approximate_morse_symbol_from_ms(button_held_duration_ms);
            }

            // Output the translated morse code
            morse_symbol_buffer[morse_symbol_buffer_index] = '\0';  // null terminate
            ascii_buffer[ascii_buffer_index] = '\0'; // null terminate
            printf("\033[2J\033[H");  // clear screen

            printf("%s\n", ascii_buffer); // Output the ascii buffer
            printf("%s", morse_symbol_buffer); // Output the morse buffer
        }
    }
}
