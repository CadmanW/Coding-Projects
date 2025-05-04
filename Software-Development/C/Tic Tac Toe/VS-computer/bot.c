// Does the computer's turn
void do_computer_turn(int board[9], int computerLetter);

// Algorithm for picking the best move
int minimax(int board[9], int scores[9], int computerLetter);

void do_computer_turn(int board[9], int computerLetter) {
    int scores[9] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
    minimax(board, scores, computerLetter);
}

int minimax(int board[9], int scores[9], int computerLetter) {

    // don't think my current understanding of minimax is good enough,
    // WRITE PSUDO CODE FIRST

    // Check every tile
    for (int i = 0; i < 9; i++) {
        // if it's an Empty tile
        if (board[i] == 0) {
            // Move here
            board[i] = computerLetter;

            // Set scores for win conditions
            if (check_for_win(board, computerLetter)) {
                scores[i] = 1;
            }
            else if (check_for_win(board, computerLetter)) {
                scores[i] = -1;
            }
        }
    }
    return 0;
}
