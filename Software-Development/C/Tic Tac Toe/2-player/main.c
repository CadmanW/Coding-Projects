#include <stdio.h>

void display_board (char board[3][3]);
int do_player_turn(char player, char board[3][3]);
char check_win(char board[3][3]);
void convert_board_to_bitmap(char board[3][3], int board_bitmap[3][3]);

int main(void) {

    char board[3][3] = {
        {'1', '2', '3'},
        {'4', '5', '6'},
        {'7', '8', '9'}
    };
    int play_game = 1;

    // Main game loop
    // player_turn will return a 1 to continue the game, and a 0 to stop the game, based on if someone wins or not, or if there is a tie
    while (play_game) {
        if (do_player_turn('X', board) || do_player_turn('O', board)) {
            play_game = 0;
        }
    }

    return 0;
}








void display_board(char board[3][3]) {
    printf("\033[H\033[J");
    printf("+-----------+\n");
    printf("| %c | %c | %c |\n", board[0][0], board[0][1], board[0][2]);
    printf("|-----------|\n");
    printf("| %c | %c | %c |\n", board[1][0], board[1][1], board[1][2]);
    printf("|-----------|\n");
    printf("| %c | %c | %c |\n", board[2][0], board[2][1], board[2][2]);
    printf("+-----------+\n");
}

int do_player_turn(char player, char board[3][3]) {
    int input;
    int x;
    int y;
    int winner;
    int board_bitmap[3][3];
    convert_board_to_bitmap(board, board_bitmap);
    int get_input = 1;
    

    display_board(board);
    printf("\nChoose a square\n");
    printf("============================\n");
    printf("%c's turn\n> ", player);

    // Get input
    while (get_input) {

        scanf("%i", &input);
        y = (input / 3);
        x = (input % 3) - 1;

        // Validate input
        if (input >= 1 && input <= 9) {
            // Make sure the chosen space hasn't been taken
            if (board[y][x] != 'X' && board[y][x] != 'O') {
                board[y][x] = player;
                get_input = 0;
            }
            else {
                printf("This space has already been taken! Try again\n> ");
            }
        }
        else {
            printf("Invalid input. Try again\n> ");
        }
    }

    // check_win returns the character of the winning player, 'X' or 'O'
    winner = check_win(board);

    // If there's a winner, stop game
    if (winner == 'X' || winner == 'O') {
        display_board(board);
        printf("\n====================\n");
        printf("%c won!!\n", winner);
        return 1;
    }
    else if (winner == 'T') {
        display_board(board);
        printf("\n====================\n");
        printf("Tie! nobody won.\n");
        return 1;
    }

    // if there's no winner, continue game
    return 0;
}

char check_win(char board[3][3]) {
    // Convert the board to a bitmap: 'X' = 1; 'O' = -1; ' ' = 0
    // If all the numbers in the line add up to either 3 or -3, this indicated a winner of 'X' for 3 and 'O' for -3
    int board_bitmap[3][3];
    convert_board_to_bitmap(board, board_bitmap);

    // Check the rows
    for (int i = 0; i < 3; i++) {
        int res = board_bitmap[i][0] + board_bitmap[i][1] + board_bitmap[i][2];
        if (res == 3) return 'X';
        else if (res == -3) return 'O';
    }

    // Check the columns
    for (int i = 0; i < 3; i++) {
        int res = board_bitmap[0][i] + board_bitmap[1][i] + board_bitmap[2][i];
        if (res == 3) return 'X';
        else if (res == -3) return 'O';
    }

    // Check the diagonals
    int res = board_bitmap[0][0] + board_bitmap[1][1] + board_bitmap[2][2];
    if (res == 3) return 'X';
    else if (res == -3) return 'O';

    res = board_bitmap[0][2] + board_bitmap[1][1] + board_bitmap[2][0];
    if (res == 3) return 'X';
    else if (res == -3) return 'O';

    // Check for a tie
    int open_spaces = 0;
    for (int y = 0; y < 3; y++) {
        for (int x = 0; x < 3; x++) {
            if (board_bitmap[y][x] == 0) open_spaces++;
        }
    }
    if (open_spaces == 0) return 'T';

    // default case, nobody wins and no tie
    return '0';
}

void convert_board_to_bitmap(char board[3][3], int board_bitmap[3][3]) {
    for (int y = 0; y < 3; y++) {
        for (int x = 0; x < 3; x++) {
            switch (board[y][x]) {
                case 'X':
                    board_bitmap[y][x] = 1;
                    break;

                case 'O':
                    board_bitmap[y][x] = -1;
                    break;

                default:
                    board_bitmap[y][x] = 0;
            }
        }
    }
}
