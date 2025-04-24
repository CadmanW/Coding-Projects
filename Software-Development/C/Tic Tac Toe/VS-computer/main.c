#include <stdio.h>
#include "functions.c"
#include "bot.c"

int main(void) {

    // 1 = 'X', 0 = ' ', -1 = 'O'
    int board[3][3] = {
        {0, 0, 0},
        {0, 0, 0},
        {0, 0, 0}
    };
    // single character input
    char input;
    int playerLetter;
    int getInput = 1;
    // Using pointers to the turn functions so that the player can choose if they want to go first or second
    void(*do_player_one_turn)(int board[3][3], int playerLetter);
    void(*do_player_two_turn)(int board[3][3], int playerLetter);

    clear_terminal();

    do {
        printf("Would you like to go first? ( y | n )\n> ");
        scanf(" %c", &input);
        if (input == 'y') {
            do_player_one_turn = &do_human_turn;
            do_player_two_turn = &do_computer_turn;
            getInput = 0;
        }
        else if (input == 'n') {
            do_player_two_turn = &do_computer_turn;
            do_player_one_turn = &do_human_turn;
            getInput = 0;
        }
        else {
            printf("\nPlease type either: lowercase 'y' or lowercase 'n'\n");
            getInput = 1;
        }
    } while (getInput);

    do {
        // Let player choose their prefered letter
        printf("Which letter would you like? ( X | O )\n> ");
        scanf(" %c", &input);

        switch (input) {
            case 'X':
                playerLetter = 1;
                getInput = 0;
                break;

            case 'O':
                playerLetter = -1;
                getInput = 0;
                break;

            default:
                printf("\nPlease type either: uppercase 'X' or uppercase 'O'\n");
                getInput = 1;
        }

    } while (getInput);


    // Main game loop, runs 9 times (so we don't have to check for a tie after every move. This loop will end when the board is full; after 9 turns)
    for (int i = 0; i < 9; i++) {
        // alternate who's turn it is
        if (i % 2 == 0) {
            (*do_player_one_turn)(board, playerLetter);
            if (check_for_win(board, playerLetter)) {
                break;
            }
        }
        else {
            (*do_player_two_turn)(board, playerLetter);
            if (check_for_win(board, playerLetter)) {
                break;
            }
        }
    }
}







