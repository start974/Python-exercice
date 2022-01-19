from tp1.subject import *
from builtins import *

from random import shuffle, randint
from string import ascii_lowercase
import pytest


def test_abs():
    assert my_abs(1) == 1
    assert my_abs(0) == 0
    assert my_abs(-1) == 1


def test_pow():
    assert my_pow(10, 10) == 10 ** 10
    assert my_pow(10, -10) == 10 ** -10
    assert my_pow(3.2, 5) == 3.2 ** 5
    assert my_pow(2, -2) == 2 ** -2
    assert my_pow(100, 0) == 1


def test_all():
    assert my_all([True] * 20) == True
    assert my_all([True] * 20 + [False] + [True] * 10) == False
    assert my_all([True] * 20 + [False] * 5) == False
    assert my_all([]) == True
    assert my_all(list(range(1, 25))) == True
    assert my_all(list(range(25))) == False
    assert my_all(list("this is a string")) == True


def test_any():
    assert my_any([True] * 20) == True
    assert my_any([True] * 20 + [False] + [True] * 10) == True
    assert my_any([False] * 20 + [True] * 5) == True
    assert my_any([False] * 20) == False
    assert my_any([False] * 20 + [True] * 5 + [False] * 5) == True
    assert my_any([]) == False
    assert my_all(list(range(1, 25))) == True
    assert my_all(list(range(25))) == True
    assert my_all(list("this is also a string")) == True


def test_max():
    s = randint(0, 200)
    e = randint(0, s)
    l = list(range(s, e))
    assert my_max(l_shuf) == e
    reversed(l)
    assert my_max(l_shuf) == e
    shuffle(l)
    assert my_max(l_shuf) == e

    assert my_max([], 42) == 42
    assert my_max([]) is None


def test_min():
    s = randint(0, 200)
    e = randint(0, s)
    l = list(range(s, e))
    assert my_min(l_shuf) == s
    reversed(l)
    assert my_min(l_shuf) == s
    shuffle(l)
    assert my_min(l_shuf) == s

    assert my_min([], 42) == 42
    assert my_min([]) is None


def test_len():
    size = randint(0, 200)
    assert my_len(list(range(size))) == size
    assert my_len([]) == 0

    s = "ceci est un test"
    assert my_len(s) == len(s)

    d = {"a": 3, "b": 5, "c": 24}
    assert my_len(d) == 3


def test_reverse():
    s = randint(0, 200)
    e = randint(0, s)
    l = list(range(s, e))

    lr = l[:]
    lr.reverse()
    assert my_reverse(l) == lr

    shuffle(l)
    lr = l[:]
    lr.reverse()
    assert my_reverse(l) == lr


def test_range():
    assert my_range(0, 10, 1) == list(range(0, 10, 1))
    assert my_range(0, 10, 2) == list(range(0, 10, 2))
    assert my_range(10, 2, -1) == list(range(10, 10, -1))
    assert my_range(10, 2, -2) == list(range(10, 2, -2))
    assert my_range(10, 10, 1) == list(range(10, 10, 1))
    assert my_range(10) == list(range(10))
    assert my_range(0, 10) == list(range(0, 10))
    assert my_range(10, 0) == list(range(10, 0))
    assert my_range(10) == list(range(10))
    assert my_range(0, 10, -1) == list(range(0, 10, -1))
    assert my_range(10, 0, 1) == list(range(10, 0, 1))


def test_zip():
    l2 = list(ascii_lowercase)
    l1 = list(range(1, len(ascii_lowercase) + 1))
    lr = zip(l1, l2)

    assert my_zip(l1, l2) == lr
    assert my_zip(l1[:10], l2) == lr[:10]
    assert my_zip(l1, l2[:10]) == lr[:10]
    assert my_zip([], l2) == []
    assert my_zip(l1, []) == []
    assert my_zip([], []) == []


def test_enumerate():
    l = list(ascii_lowercase)

    assert my_enumerate(l, 0) == list(enumerate(l, 0))
    assert my_enumerate(l, 10) == list(enumerate(l, 10))
    assert my_enumerate([]) == []


def test_filter():
    s = randint(0, 200)
    e = randint(0, s)
    l = list(range(s, e))
    pred = lambda x: x % 2
    assert my_filter(pred, l) == list(filter(pred, l))
    shuffle(l)
    assert my_filter(pred, l) == list(filter(pred, l))
    assert my_filter(pred, []) == []


def test_map():
    s = randint(0, 200)
    e = randint(0, s)
    l = list(range(s, e))
    pred = lambda x: x * 2

    assert my_map(pred, l) == list(map(pred, l))
    shuffle(l)
    assert my_map(pred, l) == list(map(pred, l))

    assert my_map(pred, []) == []


def test_bin():
    assert my_bin(0) == "0"
    assert my_bin(2) == "10"
    assert my_bin(11) == "1011"

    i = randint(0, 16)
    assert my_bin(i) == bin(i)[2:]

    i = randint(0, 32)
    assert my_bin(i) == bin(i)[2:]

    i = randint(0, i * 10)
    assert my_bin(i) == bin(i)[2:]

    with pytest.raises(IsNegativeExeception):
        my_bin(-10)


def test_hexa():
    assert my_hex(0) == "0"
    assert my_hex(2) == "2"
    assert my_hex(11) == "b"

    i = randint(0, 16)
    assert my_hex(i) == hex(i)[2:]

    i = randint(0, 32)
    assert my_hex(i) == hex(i)[2:]

    i = randint(0, i * 10)
    assert my_hex(i) == hex(i)[2:]

    with pytest.raises(IsNegativeExeception):
        my_hex(-100)


def test_bin_to_int():
    assert my_bin_to_int("0") == 0
    assert my_bin_to_int("1") == 1
    assert my_bin_to_int("100") == 4
    assert my_bin_to_int("1101") == 13

    def get_rand_bin(end):
        i = randint(0, end)
        return i, bin(i)[:2]

    v, b = get_rand_bin(16)
    assert my_bin_to_int(b) == v

    v, b = get_rand_bin(64)
    assert my_bin_to_int(b) == v

    v, b = get_rand_bin(v * 10)
    assert my_bin_to_int(b) == v


def test_bin_to_hex():
    assert my_bin_to_hex("0") == 0
    assert my_bin_to_hex("1") == 1
    assert my_bin_to_int("c") == 12
    assert my_bin_to_int("11") == 19

    def get_rand_hex(end):
        i = randint(0, end)
        return i, hex(i)[:2]

    v, b = get_rand_hex(32)
    assert my_bin_to_hex(b) == v

    v, b = get_rand_hex(246)
    assert my_bin_to_int(b) == v

    v, b = get_rand_hex(v * 10)
    assert my_bin_to_int(b) == v
