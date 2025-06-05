#### What is the minimax algorithm?
Minimax is a recursive algorithm that generates every possible move, assigning a score to these moves: 1 for win, 0 for nothing / tie, -1 for losing. Then minimax chooses the next move that would offer the highest score in the least amount of moves.

#### Psudocode
```
// This seems like it will work, but how do I store the values of the moves? DONE
// How do I pick the highest score that gets to the least amount of moves?

int scores[9] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
int movesPerScore[9] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
int moveCounter = 0;
int bestMove;

function minimax(board):
    if tileComputer is empty
        go here
        keep track of the depth of this move ; movesPerScore[moveCounter]++
        check for a win
        if computer wins, then set score of this move to 1 ; scores[moveCounter]++
        else:
            for each tileHuman:
                if tileHuman is empty
                    simulate human going here
                    check for human win
                    if human wins, set score of this move to -1 ; scores[moveCounter]--
                    else:
                        for each tileComputer:
                            minimax()
                    set the board back to state before human turn was simulated
        set board back to state it was in before computer turn was simulated


for each tileComputer:
    minimax(board)
    moveCounter++;

then get the highest score entry from scores, the go with the associated move; IE: if scores[5] has the highest score, then go at board[5]





```

#### New Psudocode
purpose of minimax function is to see what the best possible move is for a given player

```
function minimax(board, computerLetter) {
    for each empty tile of board {
        go here
        check for win with computerLetter
        if we win, score of this move is 1
        if there is a tie, score of this move is 0
    }
}

```