from .exceptions import IsNegativeException
from typing import TypeVar, Optional, Iterable, Callable

"""
Ce TP parle de conversion entre plusieurs base 10, 2 et 16
"""


def from_int(i: int, base, mapping_string) -> str:
    if i < 0:
        raise IsNegativeException()
    if i == 0:
        return mapping_string[0]
    res = ""
    while i > 0:
        res = mapping_string[i % base] + res
        i //= base
    return res


def my_bin(i: int) -> str:
    """
    renvoie une string correspondant à l'entier en binaire donnée en argument
    (dans notre cas nous ajouteront pas 0b comme fait par python
    et nous ne géreront pas les entier négatif)
    :param i: entier a convertir
    :return: binaire correspondant
    :raise: ISNegativeException si i est négatif
    """
    return from_int(i, 2, "01")


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
    return from_int(i, 16, string_hexa)


def to_int(s: str, base, mapping_string) -> int:
    mapping = {k: v for (v, k) in enumerate(mapping_string)}
    coef = 1
    res = 0
    for x in reversed(s):
        res += mapping[x] * coef
        coef *= base
    return res


def my_bin_to_int(s: str) -> int:
    """
    equivalent a `int(x, 2)`
    :param s: string d'un binaire positif à convertir en base 10
    :return: entier en base 10
    """
    return to_int(s, 2, "01")


def my_hex_to_int(s: str) -> int:
    """
    equivalent a `int(x, 16)`
    :param s: string d'un hexadécimal positif à convertir en base 10
    :return: entier en base 10
    """
    return to_int(s, 16, string_hexa)
