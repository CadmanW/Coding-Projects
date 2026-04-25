/**
 * Copyright (c) 2020 Raspberry Pi (Trading) Ltd.
 *
 * SPDX-License-Identifier: BSD-3-Clause
 */

#include <stdio.h>
#include "pico/stdlib.h"

int main() {
    stdio_usb_init();
    while (true) {
        printf("Hello, world!\n");
        sleep_ms(1000);
    }
}
