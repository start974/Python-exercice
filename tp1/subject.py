from .exceptions import IsNegativeException
from .remove_builtins import *
from typing import TypeVar, Optional, Iterable, Callable

T = TypeVar('T')
U = TypeVar('U')
'''
My builtin function  python
---
Le but du tp est de recrée fonction buitin de python (https://docs.python.org/3/library/functions.html).

Nous n'utiliseront pas list itérable dans notre cas mais des lists

Nous utilisont donc aucune construction des buitins de python dans ce fichier.

'''


def my_abs(x: int) -> int:
    """
    renvoie la valeur absolue d'un entier
    :param x: entier a traiter
    :return: |x|
    """
    return x if x > 0 else -x


def my_pow(a: float, b: int) -> float:
    """
    fait le calcul de a^b
    :param a: float à mettre à la puissance
    :param b: entier de puissance (peut etre négatif)
    :return: a ^ b
    """
    neg = b < 0
    if neg:
        b = my_abs(b)
    res = 1
    while b != 0:
        if b % 2 == 1:
            res *= a
        a *= a
        b //= 2
    if neg:
        return 1 / res
    return res


# --------------------------------------------------
# |             opération avec les itéateur        |
# --------------------------------------------------

def my_all(l: list[T]) -> bool:
    """
    renvoie vrais si chaque élément de la liste est True
    :key: (utilisé `bool(x)` pour convertir un élément x en booléen )
    :param l: list à itéré
    :return: bool
    """
    pass


def my_any(l: list[T]) -> bool:
    """
    renvoie vrais au moins un élément de la liste est True
    :key: (utilisé `my_bool(x)` pour convertir un élément x en booléen )
    :param l: list à itéré
    :return: bool
    """
    pass


def my_max(l: list[int], default: Optional[int] = None) -> int:
    """
    maximum d'une liste en utilisant l'opérateur ">"
    :param l: list a choisir le max
    :param default: TODO
    :return: entier le plus grand
    """
    pass


def my_min(l: list[int], default: Optional[int] = None) -> int:
    """
    minimum d'une liste en utilisant l'opérateur "<"
    :param l: list a choisir le max
    :param default: TODO
    :return: entier le plus grand
    """
    pass


def my_sum(l: list[int], start: int = 0) -> int:
    """
    somme une list de d'entier
    :param l: list a sommé
    :param start: valeur de base
    :return: somme des éléments
    """
    pass


def my_len(a: Iterable) -> int:
    """
    prend renvoie la longeur d'une liste
    :param a: élément itérable
    :return: longueur de l'intérable
    :key: TODO: Est ce que votre fonction fonctionne aussi pour toute structure itérable (dictionaire, tupple ...)?
    """
    pass


def my_reverse(l: list[T]) -> list[T]:
    """
    renvoie la liste l dans l'ordre inverse
    :param l: list a inversé
    :return: list iverse
    """
    pass


def my_range_tmp(start: int, stop: int, step: int) -> list[int]:
    """
    Cette fonction doit etre equivalent à range(start, stop, step)
    et sera utilisé pour définir le range plus classique
    :param start: borne de début
    :param stop: borne de fin (a exclure)
    :param step: pas entre 2 nombre
    :return: une list d'entier de ]start, stop[ avec un pas de step
    """
    pass


def my_range(a: int, b: int, c: int) -> list[int]:
    """
    Cette fonction colle a au range classique.
    Merci de regarder la documentation avec la commande "help(range)"
    il faut pouvoir gérer les arguments par défaut comme dans la documentation

    ex:
    range(10)
    range(1, 10)
    range(1, 20, 30)
    """
    pass


def my_zip(l1: list[T], l2: list[U]) -> list[tuple[T, U]]:
    """
    crée une liste de tupple contenant en parallèlle les élément de l1 et l2
    :param l1: premiere liste
    :param l2: seconde liste
    :return: liste de tupple
    """
    pass


def my_enumerate(l: list[T], start: int) -> list[tuple[int, T]]:
    """
    similaire a "enumerate"
    crée une list de tupple avec l'indice et le suivit de l'élément
    (attention a bien changer certain argument en par défaut
    pour avoir le meme conporment que énumérate)
    :param l: list to enumerate
    :param start: debut des indice
    :return: list of tupple index, elements
    """
    pass


def slice(l: list[T], start: int, stop: int, step: int = 1) -> list[T]:
    """
    revoie la copie de la liste de l'indice start a stop
    si stop est supérieur a la list on s'arrete avant
    :key: eauivalent to l[start:stop:step]
    :param l: list a couper
    :param start: indice de début
    :param stop: indice de fin
    :param step: pas entre chaque indicde
    :return: copie de la list couper
    """
    pass


def my_filter(predicate: Callable[[T], bool], l: list[T]) -> list[T]:
    """
    cette fonction filtre les élément qui ne valide pas le prédicat.
    :key
    Pour utiliser le prédicat il faut juste faire: `predicat(x)` ou x est l'élément à testé
    :param predicate: predicat a utiliser (T -> bool)
    :param l: list a filtré
    :return: list des élément filtré
    """
    pass


def my_map(f: Callable[[T], U], l: list[T]) -> list[U]:
    """
    cette fonction applique la fonction f a tout les élément de la liste et la renvoie
    :key
    Pour utiliser le f il faut juste faire: `f(x)` ou x est l'élément à convertir
    :param f: fonction de convertion (T -> U)
    :param l: list a convertir
    :return: list des élément filtré
    """
    pass


# --------------------------------------------------
# |             conversion de nombre               |
# --------------------------------------------------


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
