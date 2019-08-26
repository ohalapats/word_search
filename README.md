**Word-Puzzle-Solver**

This is a simple console Python program that searches a grid of letters (a-z only) 
for valid English words. 
Words can be found along any diagonal, forwards, upwards, downwards 
or backwards and doesn't ‘wrap’ between edges.

To try the app just run _main.py_ file. You will be asked to input size of grid, 
after that you will see a grid of random letters and all valid words that were found in it.

To install pytest run _pip install -r requirements.txt_

To run the tests, run the appropriate command below:

Python 3.4+: _pytest test_word_search.py_

Common options:
`-v `: enable verbose output
`-x` : stop running tests on first failure
`--ff` : run failures from previous test before running other test cases
For other options, see python _-m pytest -h_
