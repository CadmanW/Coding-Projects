#include <stdio.h>
#include "functions.c"
#include "bot.c"

int main(void) {

    // 1 = 'X', 0 = ' ', -1 = 'O'
    int board[9] = {
        0, 0, 0,
        0, 0, 0,
        0, 0, 0
    };
    // single character input
    char input;
    int playerLetter;
    int getInput = 1;
    int playerTurnChosen;
    int playerOneLetter;
    int playerTwoLetter;
    // Using pointers to the turn functions so that the player can choose if they want to go first or second
    void(*do_player_one_turn)(int board[9], int playerLetter);
    void(*do_player_two_turn)(int board[9], int playerLetter);

    clear_terminal();

    // Getting input: Asking if player would like to go first or second
    do {
        printf("Would you like to go first? ( y | n )\n> ");
        scanf(" %c", &input);
        if (input == 'y') {
            do_player_one_turn = &do_human_turn;
            do_player_two_turn = &do_computer_turn;
            playerTurnChosen = 1;
            getInput = 0;
        }
        else if (input == 'n') {
            do_player_two_turn = &do_computer_turn;
            do_player_one_turn = &do_human_turn;
            playerTurnChosen = 2;
            getInput = 0;
        }
        else {
            printf("\nPlease type either: lowercase 'y' or lowercase 'n'\n");
            getInput = 1;
        }
    } while (getInput);

    // Getting input: asking if player wants to be 'X's or 'O's
    do {
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

        if (playerTurnChosen == 1) {
            playerOneLetter = playerLetter;
            playerTwoLetter = playerLetter * -1;
        }
        else if (playerTurnChosen == 2) {
            playerOneLetter = playerLetter * -1;
            playerTwoLetter = playerLetter;
        }

    } while (getInput);


    // Main game loop, runs 9 times (so we don't have to check for a tie after every move. This loop will end when the board is full; after 9 turns)
    for (int i = 0; i < 9; i++) {
        // alternate who's turn it is
        if (i % 2 == 0) {
            (*do_player_one_turn)(board, playerOneLetter);
            if (check_for_win(board, playerOneLetter)) {
                // Check if winning player is human or computer
                display_board(board);
                if (playerTurnChosen == 1) {
                    printf("\nYou won!!\n");
                }
                else if (playerTurnChosen == 2) {
                    printf("\nYou lost :(\n");
                }
                return 1;
            }
        }
        else {
            (*do_player_two_turn)(board, playerTwoLetter);
            if (check_for_win(board, playerTwoLetter)) {
                // Check if winning player is human or computer
                display_board(board);
                if (playerTurnChosen == 2) {
                    printf("\nYou won!!\n");
                }
                else if (playerTurnChosen == 1) {
                    printf("\nYou lost :(\n");
                }
                return 1;
            }
        }
    }
    printf("Tie! Nobody won.\n");
}
