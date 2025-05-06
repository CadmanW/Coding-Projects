#include <stdio.h>
#include "functions.c"
#include "bot.c"

int main(void) {

    int board[9] = {
        0, 0, -1,
        0, 1, 1,
        0, 0, 0
    };

    do_computer_turn(board, -1);
    
}
