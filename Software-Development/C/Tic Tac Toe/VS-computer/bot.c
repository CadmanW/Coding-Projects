// Does the computer's turn
void do_computer_turn(int board[9], int computerLetter);

// Algorithm for picking the best move
void minimax(int board[9], int scores[9], int depth[9], int moveCounter, int tileC, int computerLetter);

void do_computer_turn(int board[9], int computerLetter) {
    int scores[9] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
    int depth[9] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
    int moveCounter = 0;
    int bestMove = -1;

    // Call minimax 
    for (int tileC = 0; tileC < 9; tileC++) {
        minimax(board, scores, depth, moveCounter, tileC, computerLetter);
        moveCounter++;
    }

    for (int i = 0; i < 9; i++) {
        printf("\nscores[%i] = %i\ndepth[%i] = %i\n", i, scores[i], i, depth[i]);
    }

    for (int i = 0; i < 9; i++) {
        if (
            ((scores[i] > scores[bestMove]) ||
            ((scores[i] == scores[bestMove]) && (depth[i] < depth[bestMove])) ||
            (bestMove == -1)) &&
            board[i] == 0
        ) {
                bestMove = i;
        }
    }

    board[bestMove] = computerLetter;
}

void minimax(int board[9], int scores[9], int depth[9], int moveCounter, int tileC, int computerLetter) {
    if (board[tileC] == 0) {
        board[tileC] = computerLetter;
        if (check_for_win(board, computerLetter)) {
            scores[moveCounter]++;
        }
        else {
            depth[moveCounter]++;
            for (int tileH = 0; tileH < 9; tileH++) {
                if (board[tileH] == 0) {
                    board[tileH] = computerLetter * -1;
                    if (check_for_win(board, computerLetter * -1)) {
                        scores[moveCounter]--;
                        board[tileH] = 0;
                        break;
                    }
                    else {
                        for (int tileC = 0; tileC < 9; tileC++) {
                            minimax(board, scores, depth, moveCounter, tileC, computerLetter);
                        }
                    }
                    board[tileH] = 0;
                }
            }
        }
        board[tileC] = 0;
    }
}
