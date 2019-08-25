"""
Main module
"""
from word_search import get_valid_words, generate_grid, search_word

FILE_NAME = 'words_dict.txt'
WORDS = get_valid_words(FILE_NAME)

if __name__ == '__main__':
    grid = generate_grid(int(input("Select grid size:")))
    for i in range(len(grid)):
        print(' '.join(grid[i]))
    print(list(search_word(grid, WORDS)))
