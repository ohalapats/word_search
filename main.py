"""
Main module
"""
from argument_parser import parse_args
from word_search import get_valid_words, generate_grid, search_word

FILE_NAME = 'words_dict.txt'
WORDS = get_valid_words(FILE_NAME)

if __name__ == '__main__':
    args = parse_args()
    grid = generate_grid(args.gridsize)
    for i in range(len(grid)):
        print(' '.join(grid[i]))
    print(list(search_word(grid, WORDS)))
