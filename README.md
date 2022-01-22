# Python-exercice

This repository contain few exercies on Python.\
Subject is in directory tp** all subject files is write in French. 
And all correction is in directory
[correction](correction/)

## Setup environement

The project use [pipenv](https://pypi.org/project/pipenv/).
To install all dependency use:
```shell
$ pipenv install
```

## Run test
Tests use [pytest](https://docs.pytest.org/en/6.2.x/).
All tests is store in [tests](tests/) and it is named by tp*.py.

To run test use:
```shell
$ pipenv run pytest tests/tp*.py
```

## TP

### [TP1](tp1/subject_tmp.py) -- My Builtins functions

Objectives recreate some pythons [builtins](https://docs.python.org/3/library/functions.html) functions.
The subject file is [tp1/subject.py](tp1/subject_tmp.py)

### [TP1](tp1/subject_tmp.py) -- Base converter
Objectives is to convert positives number between base 10, 16, 2

Make function to convert :
- Base 10 -> binary
- Base 10 -> hexadecimal
- binary -> Base 10
- hexadecimal -> Base 10
