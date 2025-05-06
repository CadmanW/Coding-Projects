// prints an ANSI code to the terminal that moves the cursor to top left, then clears everything after the cursor
void clear_terminal(void);

// Displays the board to the player
void display_board(int board[9]);

// Turns the board of integers into characters to be displayed to the player
void get_char_board(int board[9], char char_board[9]);

// Does the human's turn
void do_human_turn(int board[9], int playerLetter);

// Check for a win, handle it (including output and user interaction for a game ended scenario), and return 1 if the game should end, 0 to continue
int check_for_win(int board[9], int playerLetterToCheck);







void clear_terminal(void) {
    printf("\033[H\033[J");
}

void display_board(int board[9]) {
    // Turn the numbers from board to the corresponding letters: 1 = X, 0 = _, -1 = O
    char char_board[9];
    get_char_board(board, char_board);

    clear_terminal();
    
    printf("+---+---+---+\n");
    printf("| %c | %c | %c |\n", char_board[0], char_board[1], char_board[2]);
    printf("+---+---+---+\n");
    printf("| %c | %c | %c |\n", char_board[3], char_board[4], char_board[5]);
    printf("+---+---+---+\n");
    printf("| %c | %c | %c |\n", char_board[6], char_board[7], char_board[8]);
    printf("+---+---+---+\n");
}

void get_char_board(int board[9], char char_board[9]) {
    // Iterate through board and assign the corresponding index in char_board 
    for (int i = 0; i < 9; i++) {
        switch(board[i]) {
            case 1:
                char_board[i] = 'X';
                break;

            case -1:
                char_board[i] = 'O';
                break;

            default:
                char_board[i] = i + '0'; // add '0' to convert from int to char
        }
    }
}


void do_human_turn(int board[9], int playerLetter) {

    int getInput = 1;
    int input;

    display_board(board);


    // Get input: ask where the play would like to go for their turn
    printf("Your turn, pick a square's number to put your letter there:\n> ");

    do {
        scanf(" %i", &input);

        // Make sure the chosen space hasn't been taken
        if (board[input] == 0 && input <= 8 && input >= 0) {
            board[input] = playerLetter;
            getInput = 0;
        }
        else {
            printf("Invalid Input. Please try again:\n> ");
        }
    } while (getInput);
}

int check_for_win(int board[9], int playerLetterToCheck) {
    int possibleWinPatterns[8][3] = {
        // Rows
        {0, 1, 2},
        {3, 4, 5},
        {6, 7, 8},

        // Columns
        {0, 3, 6},
        {1, 4, 7},
        {2, 5, 8},

        // Diagonals
        {0, 4, 8},
        {6, 4, 2}
    };

    // iterate through possibleWinPatterns to check for a win in each pattern by adding the numbers in the win pattern
    for (int y = 0; y < 8; y++) {
        int sum = 0;
        for (int x = 0; x < 3; x++) {
            sum += board[possibleWinPatterns[y][x]];
        }
        if (sum == playerLetterToCheck * 3) {
            // If playerx wins, return 1
            return 1;
        }
    }
    // If playerx did not win, return 0;
    return 0;
}
