# HangmanSolver
Solver for the hangman game


To use:

Clone repository

http: `git clone https://github.com/carter144/HangmanSolver.git`


ssh: `git clone git@github.com:carter144/HangmanSolver.git`

cd to folder: `cd HangmanSolver`

run with `python hangmanSolver.py`

The script will ask for an input for the number of characters you are trying to guess.

Once entered, start guessing letters and enter them into the program (0 indexed).

For example:

If there is the letter 'a' in the first character enter: `a 0` 
If the letter 'e' does not exist in the puzzle enter `e -1`

Each time a letter is entered there will be a dictionary that shows which is the next frequent character that you should guess.
