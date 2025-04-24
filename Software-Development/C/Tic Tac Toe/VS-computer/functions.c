// prints an ANSI code to the terminal that moves the cursor to top left, then clears everything after the cursor
void clear_terminal(void);

// Displays the board to the player
void display_board(int board[3][3]);

// Turns the board of integers into characters to be displayed to the player
void get_char_board(int board[3][3], char char_board[3][3]);

// Does the human's turn
void do_human_turn(int board[3][3], int playerLetter);

//check for a win, handle it (including output and user interaction for a game ended scenario), and return 1 if the game should end, 0 to continue
int check_for_win(int board[3][3], int playerLetter);







void clear_terminal(void) {
    printf("\033[H\033[J");
}

void display_board(int board[3][3]) {

    char char_board[3][3];
    get_char_board(board, char_board);

    clear_terminal();
    
    printf("+---+---+---+\n");
    printf("| %c | %c | %c |\n", char_board[0][0], char_board[0][1], char_board[0][2]);
    printf("+---+---+---+\n");
    printf("| %c | %c | %c |\n", char_board[1][0], char_board[1][1], char_board[1][2]);
    printf("+---+---+---+\n");
    printf("| %c | %c | %c |\n", char_board[2][0], char_board[2][1], char_board[2][2]);
    printf("+---+---+---+\n");
}

void get_char_board(int board[3][3], char char_board[3][3]) {
    // n keeps track of which tile the loop is on, so if it's an empty square, the correct tile number will be set to said tile
    int n = 1;
    for (int y = 0; y < 3; y++) {
        for (int x = 0; x < 3; x++) {
            switch(board[y][x]) {
                case 1:
                    char_board[y][x] = 'X';
                    break;

                case -1:
                    char_board[y][x] = 'O';
                    break;

                default:
                    char_board[y][x] = n + '0'; // add '0' to convert from int to char
            }
            n++;
        }
    }
}


void do_human_turn(int board[3][3], int playerLetter) {

    int getInput = 1;
    int input;
    int y;
    int x;

    display_board(board);

    printf("Your turn, pick a square's number to put your letter there:\n> ");

    do {
        scanf("%i", &input);


        y = input / 3;
        x = (input % 3) - 1; // -1 to make index start at 0 instead of 1, picks the correct tile

        // Make sure the chosen space hasn't been taken
        if (board[y][x] == 0 && input <= 9 && input >= 1) {
            board[y][x] = playerLetter;
            getInput = 0;
        }
        else {
            printf("Invalid Input. Please try again:\n> ");
        }
    } while (getInput);
}

int check_for_win(int board[3][3], int playerLetter) {
    int possibleWinPatterns[8][3][2] = {
        // Rows
        {{0, 0}, {0, 1}, {0, 2}},
        {{1, 0}, {1, 1}, {1, 2}},
        {{2, 0}, {2, 1}, {2, 2}},

        // Columns
        {{0, 0}, {1, 0}, {2, 0}},
        {{0, 1}, {1, 1}, {2, 1}},
        {{0, 2}, {1, 2}, {2, 2}},

        // Diagonals
        {{0, 0}, {1, 1}, {2, 2}},
        {{2, 0}, {1, 1}, {0, 2}}
    };

    for (int y = 0; y < 8; y++) {
        int sum = 0;
        for (int x = 0; y < 3; y++) {
            sum += board[possibleWinPatterns[y][x][0]][possibleWinPatterns[y][x][1]];
        }
        switch (sum) {
            case 3:
                return 1;
                break;
            case -3:
                return -1;
                break;
        }
    }

    return 0;
}

// FINISH REFACTORING CHECK WIN
