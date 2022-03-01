#from correction.tp1.subject import *
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
    def is_close(a, b, eps=1E-4):
        return abs(a - b) <= eps

    assert my_pow(10, 10) == 10 ** 10
    assert my_pow(10, -10) == 10 ** -10
    assert my_pow(2, -2) == 2 ** -2

    assert is_close(my_pow(3.2, 5), 3.2 ** 5)

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
    assert my_any(list(range(1, 25))) == True
    assert my_any(list(range(25))) == True
    assert my_any(list("this is also a string")) == True


def test_max():
    e = randint(0, 200)
    s = randint(0, e)
    l = list(range(s, e + 1))
    assert my_max(l) == e
    reversed(l)
    assert my_max(l) == e
    shuffle(l)
    assert my_max(l) == e

    assert my_max([], 42) == 42
    assert my_max([]) is None


def test_min():
    e = randint(0, 200)
    s = randint(0, e)
    l = list(range(s, e + 1))
    assert my_min(l) == s
    reversed(l)
    assert my_min(l) == s
    shuffle(l)
    assert my_min(l) == s

    assert my_min([], 42) == 42
    assert my_min([]) is None


def test_sum():
    e = randint(0, 200)
    s = randint(0, e)
    l = list(range(s, e))
    res = sum(l)
    assert my_sum(l) == res
    reversed(l)
    assert my_sum(l) == res
    shuffle(l)
    assert my_sum(l) == res
    assert my_sum(l, 10) == res + 10


def test_len():
    size = randint(0, 200)
    assert my_len(list(range(size))) == size
    assert my_len([]) == 0

    s = "ceci est un test"
    assert my_len(s) == len(s)

    d = {"a": 3, "b": 5, "c": 24}
    assert my_len(d) == 3


def test_reverse():
    e = randint(0, 200)
    s = randint(0, e)
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
    assert my_range(10, 2, -1) == list(range(10, 2, -1))
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
    lr = list(zip(l1, l2))

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


def test_splice():
    l = list(range(25))

    assert my_slice(l, 0, len(l)) == l
    assert my_slice(l, 0) == l
    assert my_slice(l, 1, 10) == l[1:10]
    assert my_slice(l, 1, 10, 2) == l[1:10:2]
    assert my_slice(l, 1, -1) == l[1:-1]
    assert my_slice(l, -3, -1) == l[-3:-1]


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
