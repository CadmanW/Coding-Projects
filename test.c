#include <stdio.h>
#include <string.h>

// Scrambles/Descrambles input using XOR with 0x5A
void xor_transform(const unsigned char *input, char *output, size_t length) {
    for (size_t i = 0; i < length; i++) {
        output[i] = input[i] ^ 0x5A;
    }
    output[length] = '\0'; // Ensure null-termination for strings
}

int main() {
    // Scrambled password from the Rust source
    unsigned char scrambled_password[] = {
        0x1A, 0x2B, 0x3E, 0x3E, 0x21, 0x6B, 0x79, 0x69,
        0x1A, 0x79, 0x6B, 0x21, 0x7B, 0x21, 0x69, 0x79
    };
    size_t pass_len = sizeof(scrambled_password);

    // Encoded flag
    unsigned char encoded_flag[] = {
        0x19, 0x34, 0x2E, 0x29, 0x7B, 0x66, 0x30, 0x2E,
        0x36, 0x33, 0x5F, 0x74, 0x68, 0x33, 0x5F, 0x6B,
        0x33, 0x79, 0x7D, 0x00
    };
    size_t flag_len = sizeof(encoded_flag);

    char input[256];
    printf("Enter password: ");
    
    // Read input and remove newline character
    if (fgets(input, sizeof(input), stdin)) {
        input[strcspn(input, "\n")] = 0;
    }

    size_t input_len = strlen(input);

    // Check if length matches first to avoid buffer issues
    int access_granted = 0;
    if (input_len == pass_len) {
        access_granted = 1;
        for (size_t i = 0; i < pass_len; i++) {
            if ((unsigned char)(input[i] ^ 0x5A) != scrambled_password[i]) {
                access_granted = 0;
                break;
            }
        }
    }

    if (access_granted) {
        char flag[flag_len + 1];
        xor_transform(encoded_flag, flag, flag_len);
        printf("Access granted! Flag: %s\n", flag);
    } else {
        printf("Access denied!\n");
    }

    return 0;
}