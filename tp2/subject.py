from .exceptions import IsNegativeException
from typing import TypeVar, Optional, Iterable, Callable

"""
Ce TP parle de conversion entre plusieurs base 10, 2 et 16
"""
def my_bin(i: int) -> str:
    """
    renvoie une string correspondant à l'entier en binaire donnée en argument
    (dans notre cas nous ajouteront pas 0b comme fait par python
    et nous ne géreront pas les entier négatif)
    :param i: entier a convertir
    :return: binaire correspondant
    :raise: ISNegativeException si i est négatif
    """
    pass


string_hexa = "0123456789abcdef"


def my_hex(i: int) -> str:
    """
    renvoie une string correspondant à l'entier en hexadécimal donnée en argument
    (dans notre cas nous ajouteront pas 0x comme fait par python
    et nous ne géreront pas les entier négatif)
    :param i: entier a convertir
    :return: hexadécimal correspondant
    :raise: ISNegativeException si i est négatif
    """
    pass


def my_bin_to_int(s: str) -> int:
    """
    equivalent a `int(x, 2)`
    :param s: string d'un binaire positif à convertir en base 10
    :return: entier en base 10
    """
    pass


def my_hex_to_int(s: str) -> int:
    """
    equivalent a `int(x, 16)`
    :param s: string d'un hexadécimal positif à convertir en base 10
    :return: entier en base 10
    """
    pass
