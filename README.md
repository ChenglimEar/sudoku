# Solve Sudoku using backtracking

This is a simple script on how we can easily solve Sudoku using backtracking.

The idea is simple.  We traverse through all open slots and test out all the possible numbers (1-9).  As we reach a working number, we add the number to the board at the current open position and move on to the next open position.  We do the same thing for the next open position and move forward until we either find a working number for the last open position or we find a position with no working number.  When we find a position with no working number, we backtrack to the previous open position that we placed a number in and remove the number. We try to find another number to place in that position.  If there's no number left, we backtrack again.  If there is another number that works, we place that number on the board and move forward to the next open position and continue as before.

Simply run solve.py to see the code at work:

```
python solve.py
```
