from tp2.subject import *

from random import shuffle, randint
from string import ascii_lowercase
import pytest


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

    with pytest.raises(IsNegativeException):
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

    with pytest.raises(IsNegativeException):
        my_hex(-100)


def test_bin_to_int():
    assert my_bin_to_int("0") == 0
    assert my_bin_to_int("1") == 1
    assert my_bin_to_int("100") == 4
    assert my_bin_to_int("1101") == 13

    def get_rand_bin(end):
        i = randint(0, end)
        return i, bin(i)[2:]

    v, b = get_rand_bin(16)
    assert my_bin_to_int(b) == v

    v, b = get_rand_bin(64)
    assert my_bin_to_int(b) == v

    v, b = get_rand_bin(v * 10)
    assert my_bin_to_int(b) == v


def test_bin_to_hex():
    assert my_hex_to_int("0") == 0
    assert my_hex_to_int("1") == 1
    assert my_hex_to_int("c") == 12
    assert my_hex_to_int("15") == 21

    def get_rand_hex(end):
        i = randint(0, end)
        return i, hex(i)[2:]

    v, b = get_rand_hex(32)
    assert my_hex_to_int(b) == v

    v, b = get_rand_hex(246)
    assert my_hex_to_int(b) == v

    v, b = get_rand_hex(v * 10)
    assert my_hex_to_int(b) == v
