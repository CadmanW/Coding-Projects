// Does the computer's turn
void do_computer_turn(int board[3][3], int playerLetter);

// Algorithm for picking the best move
int minimax(int board[3][3], int playerLetter);

void do_computer_turn(int board[3][3], int playerLetter) {

    return minimax(board, playerLetter);
}

int minimax(int board[3][3], int playerLetter) {
    int score;

    // Check every tile for a possible move
    for (int y = 0; y < 3; y++) {
        for (int x = 0; x < 3; x++) {
            if (board[y][x] == 0) {
                board[y][x] = playerLetter * -1;

                if (check_for_win(board, playerLetter)) {
                    return playerLetter * -1;
                }
            }
        }
    }
    return 0;
}
