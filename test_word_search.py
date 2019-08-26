"""
This module contains unit tests for word search solution
"""
import pytest

from word_search import get_valid_words, generate_grid, search_word


@pytest.yield_fixture
def init_valid_words():
    file_name = 'words_dict.txt'
    words = get_valid_words(file_name)
    yield words


def test_valid_words_amount(init_valid_words):
    assert len(init_valid_words) == 62798


@pytest.mark.parametrize('grid_size', [i for i in range(2, 15)])
def test_grid_size(grid_size):
    grid = generate_grid(grid_size)
    assert len(grid) == grid_size
    for line in grid:
        assert len(line) == grid_size


def test_word_search_1(init_valid_words):
    grid = [['p', 'h', 'o'],
            ['j', 'e', 'y'],
            ['r', 'q', 't']]

    words = ['pet', 'ho', 'he', 'oh', 'eh', 'ye', 'yo', 're']

    assert list(search_word(grid, init_valid_words)) == words


def test_word_search_2(init_valid_words):
    grid = [['a', 'b', 'c', 'l', 'y'],
            ['b', 'h', 'c', 'd', 'm'],
            ['c', 'g', 'd', 'i', 'a'],
            ['d', 'i', 'k', 'm', 'x'],
            ['m', 'e', 'o', 'w', 'r']]

    words = ['ah', 'ha', 'dim', 'ma', 'my', 'mi', 'mike', 'dim', 'id', 'id', 'aid', 'ax', 'am', 'am', 'ad',
             'id', 'id', 'kid', 'mi', 'mid', 'ma', 'me', 'meow', 'mi', 'mid', 'middy', 'em', 'ow', 'woe']

    assert list(search_word(grid, init_valid_words)) == words


def test_word_search_3(init_valid_words):
    grid = [['o', 'd', 'p', 'p', 'x', 'w', 'c', 'p', 'w', 'j', 'z', 'i', 'd', 'y', 't'],
            ['j', 'n', 'x', 'g', 'p', 'x', 'w', 'c', 'a', 'i', 'q', 'j', 'k', 'n', 'r'],
            ['e', 'h', 'i', 'c', 'c', 'x', 'g', 'j', 'f', 'p', 'f', 'x', 'm', 'p', 'k'],
            ['q', 'm', 'u', 'c', 'p', 'e', 'm', 'p', 'c', 'm', 'v', 'a', 'x', 'p', 'v'],
            ['j', 'v', 'z', 'v', 'q', 'y', 'w', 'j', 'e', 'v', 'm', 'n', 'l', 'i', 'n'],
            ['z', 'b', 'e', 'x', 'd', 'g', 'p', 'j', 'f', 'y', 't', 'c', 'l', 'i', 'f'],
            ['l', 'f', 'x', 'h', 'x', 'p', 'x', 'f', 'i', 'p', 'q', 'q', 'v', 'f', 'f'],
            ['d', 'm', 'n', 'b', 'm', 'n', 'i', 'h', 'w', 'e', 'i', 'l', 'q', 'q', 'g'],
            ['i', 't', 'r', 'l', 't', 'c', 'g', 'm', 'g', 'b', 'q', 'c', 'u', 'q', 'i'],
            ['z', 'x', 'c', 'p', 'u', 'v', 'o', 'i', 's', 'a', 'w', 'n', 'n', 'u', 'v'],
            ['l', 'c', 'i', 'k', 'v', 'v', 't', 'e', 'z', 'c', 'v', 'v', 'd', 'c', 'j'],
            ['f', 'd', 'u', 'z', 'c', 'v', 'f', 'r', 'g', 'c', 'x', 'u', 'x', 'y', 'u'],
            ['h', 'p', 'n', 'h', 'p', 'f', 'l', 'j', 'c', 'k', 'j', 'q', 'h', 'e', 'y'],
            ['z', 'e', 'k', 'a', 'o', 'w', 'l', 'm', 'y', 'b', 'v', 'r', 'h', 'u', 'y'],
            ['t', 'c', 'g', 'v', 'g', 'd', 'd', 'p', 'j', 'x', 'z', 'c', 'k', 'r', 'b']]

    words = ['on', 'do', 'pa', 'pap', 'id', 'no', 'if', 'if', 'eh', 'em', 'hi', 'he', 'in', 'fa', 'pi', 'pa',
             'pap', 'fa', 'ma', 'mu', 'mi', 'me', 'um', 'uh', 'em', 'ex', 'me', 'my', 'me', 'ax', 'an', 'ax',
             'am', 'am', 'pi', 'ye', 'we', 'em', 'ma', 'my', 'la', 'in', 'if', 'nil', 'be', 'ex', 'ex', 'eh',
             'ye', 'yep', 'if', 'if', 'if', 'in', 'fix', 'he', 'pi', 'if', 'if', 'pi', 'pi', 'mi', 'in', 'if',
             'hi', 'hi', 'we', 'wife', 'lie', 'it', 'id', 'ti', 'go', 'got', 'mi', 'ms', 'mi', 'gs', 'be', 'pi',
             'up', 'is', 'it', 'saw', 'sawn', 'as', 'was', 'nu', 'nu', 'nu', 'id', 'kc', 'kc', 'to', 'tog', 'ti',
             'es', 'cab', 'cs', 'dip', 'uh', 'up', 're', 'uh', 'ye', 'he', 'nu', 'nag', 'net', 'ha', 'ho', 'hod',
             'pa', 'kc', 'kc', 'he', 'hey', 'hub', 'eh', 'eh', 'ex', 'ye', 'yuk', 'eh', 'kc', 'ah', 'an', 'and',
             'ow', 'owl', 'oak', 'of', 'off', 'oh', 'my', 'by', 'he', 'uh', 'uh', 'ye', 'ten', 'gap', 'go', 'do',
             'kc', 'rue', 'by']

    assert list(search_word(grid, init_valid_words)) == words
