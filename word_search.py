"""
This module contains word search solution
"""
import random
import string
from typing import Generator


def get_valid_words(file_name: str) -> tuple:
    """
    Get all valid words from a file

    :param file_name: Name of a file
    :return: Tuple of valid words
    """
    with open(file_name) as words_dict:
        words = words_dict.readlines()

    return tuple([word.lower().strip() for word in words])


def generate_grid(grid_size: int) -> list:
    """
    Generate grid of random letters

    :param grid_size: Length and height of a grid
    :return: List of random letters
    """
    grid = [[random.choice(string.ascii_lowercase) for _ in range(grid_size)] for _ in range(grid_size)]
    return grid


def search_word(grid: list, words: tuple) -> Generator[str, None, None]:
    """
    Search for valid words in given grid

    :param grid: Grid of letters
    :param words: Tuple of valid words
    :return: Generator object with found words
    """
    grid_size = len(grid)
    for x in range(0, grid_size):
        for y in range(0, grid_size):
            for dir_ in DIRECTIONS:
                pos = Position(x, y)
                word = ""
                for i in words:
                    while i.startswith(word) and 0 <= pos.x < grid_size and 0 <= pos.y < grid_size:
                        word += grid[pos.x][pos.y]
                        pos += dir_.move(dir_.mover)
                        if word in words:
                            yield word


class Position:
    """
    This class is a wrapper for position of a letter
    """
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)


class Direction:
    """
    This class contains methods to manipulate with words directions
    """
    def __init__(self, dir_name: str, mover: Position):
        self.dir_name = dir_name
        self.mover = mover

    @property
    def lable(self) -> str:
        """
        Direction name

        :return: Direction name
        """
        return self.dir_name

    def move(self, move_to: Position) -> Position:
        """
        Move to given position

        :param move_to: Position to move
        :return: New position
        """
        self.mover = move_to
        return self.mover


DIRECTIONS = (Direction('down', Position(0, 1)),
              Direction('up', Position(0, -1)),
              Direction('right', Position(1, 0)),
              Direction('left', Position(-1, 0)),
              Direction('down right', Position(1, 1)),
              Direction('down left', Position(-1, 1)),
              Direction('up right', Position(1, -1)),
              Direction('up left', Position(-1, -1)))
