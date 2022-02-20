from .ExceptionMatrix import *

"""
Rappelle sur les visibilité en python:
self.a: "public"
self.__a: "private"
https://www.geeksforgeeks.org/private-variables-python/

Nous allons utiliser @property pour faire des getter et des setter
https://www.programiz.com/python-programming/property
"""


class Matrix:
    def __init__(self, n: int, m: int = None, val: float = 0):
        """
        Constructeur matrice n * m
        :param n: nombres de colones
        :param m: nombre de lignes (si m = None alors m = n)
        :param val: valeur par default remplit dans la matrice (default=0)

        Matrix(2,3,1):
        1 1
        1 1
        1 1

        :exception NotNegative si n ou m est négatif

        :key: n et m n'as que des getter
        """
        if n <= 0:
            raise NotNegative("n", n)
        elif m is None:
            m = n
        elif m <= 0:
            raise NotNegative("m", m)

        self.__n = n
        self.__m = m
        self.__data = [[val] * n for _ in range(m)]

    @property
    def lines(self):
        return self.__m

    @property
    def columns(self):
        return self.__n

    @property
    def array_mat(self) -> tuple[tuple[float]]:
        """
        liste de liste d'entier représentant la matrice
        :key est une copie des donnée
        :return donné de la matrice
        """
        return tuple(tuple(val for val in line) for line in self.__data)

    @property
    def array_simple(self) -> tuple[float]:
        """
        renvoie une liste simple de notre matrice
        """
        return tuple(x for line in self.__data
                     for x in line)

    def __str__(self):
        return str(self.array_mat)

    def __repr__(self):
        width = max(map(lambda x: len(str(x)), self.array_simple)) + 2
        res = f"n:{self.lines}, m:{self.columns}\n"
        for line in self.array_mat:
            for val in line:
                res += str(val).center(width)
            res += "\n"
        return res

    def __check_line_in_range(self, i: int) -> None:
        """
        test si i a une valeur correct si non renvoie une exception
        :param i: ligne
        :exception OutOfRange
        : key useful for get and set
        """
        if not (0 <= i < self.columns):
            raise OutOfRange(0, self.columns, "Matrix.columns", i)

    def __check_column_in_range(self, j: int) -> None:
        """
        test si j a une valeur correct si non renvoie une exception
        :param j: colonne
        :exception OutOfRange
        : key useful for get and set
        """
        if not (0 <= j < self.lines):
            raise OutOfRange(0, self.lines, "Matrix.lines", j)

    def get(self, i: int, j: int) -> float:
        """
        récupère la valeur a la ligne i et a la colonne j
        :param i: ligne
        :param j: colonne
        :return: valeur trouver
        :exception OutOfRange si i ou j n'est pas dans la matrice
        """
        self.__check_line_in_range(i)
        self.__check_column_in_range(j)

        return self.__data[j][i]

    def set(self, i: int, j: int, val: int) -> None:
        """
        remplace la valeur a la ligne i et a la colonne j par val
        :param i: ligne
        :param j: colonne
        :param val: valeur a changer
        :exception OutOfRange si i ou j n'est pas dans la matrice
        """
        self.__check_line_in_range(i)
        self.__check_column_in_range(j)

        self.__data[j][i] = val

    def __eq__(self, other: object) -> bool:
        """
        implement == for matrix
        :param other: other matrix
        :return: matrix is equal
        """
        return isinstance(other, Matrix) \
               and self.lines == other.lines \
               and self.columns == other.columns \
               and self.array_simple == other.array_simple

    def get_line(self, i: int) -> [int]:
        """
        renvoie la ligne i dans une liste
        :param i: ligne a récupéré
        :return: ligne
        :exception OutOfRange si la ligne i n'est pas dans la matrice
        """
        self.__check_line_in_range(i)
        return [self.__data[i][x] for x in range(self.columns)]

    def get_column(self, j: int) -> [int]:
        """
        renvoie la colonne j dans une liste
        :param j: colonne a récupéré
        :return: colonne
        :exception OutOfRange si la colonne j n'est pas dans la matrice
        """
        self.__check_column_in_range(j)
        return [self.__data[x][j] for x in range(self.lines)]

    def __getitem__(self, key):
        """
        pour pouvoir utiliser la notation mat[...]

        mat[i: j] == get(i, j)
        mat[i:] == get_line(i)
        mat[:j] == get_column(j)
        :param key: object slice
        :return:
        """
        match key:
            case slice(start=int(i), stop=int(j), step=None):
                return self.get(i, j)
            case slice(start=int(i), stop=None, step=None):
                return self.get_line(i)
            case slice(start=None, stop=int(j), step=None):
                return self.get_column(j)
            case slice(step=int(_)):
                raise NoStep()
            case _:
                raise TypeError(f"key cannot be typed: {type(key)} (usage mat[i:j])")

    def set_line(self, i: int, line: [int]) -> None:
        """
        change toute la lignes avec les valeur de line
        :param i: ligne a modifier
        :param line: valeurs à utiliser
        :exception NotMatchSize si la longueur de la liste line ne peut pas inséré
        """
        if len(line) != self.columns:
            raise NotMatchSize(line, self.columns)
        self.__check_line_in_range(i)

        for x in range(self.columns):
            self.__data[i][x] = line[x]

    def set_column(self, j: int, col: [int]) -> None:
        """
        change toute colonne avec les valeur de column
        :param j: ligne a modifier
        :param col: valeurs à utiliser
        :exception NotMatchSize si la longueur de la liste line ne peut pas inséré
        """
        if len(col) != self.lines:
            raise NotMatchSize(col, self.lines)
        self.__check_column_in_range(j)

        for x in range(self.lines):
            self.__data[x][j] = col[x]

    def __setitem__(self, key: slice, value) -> None:
        """
        pour pouvoir utiliser la notation mat[...] = x

        mat[i: j] = x <-> set(i, j, x)
        mat[i: ] = l <-> set_line(i, l)
        mat[: j] = l <-> set_column(j, l)
        """

        match key:
            case slice(start=int(i), stop=int(j), step=None):
                self.set(i, j, value)
            case slice(start=int(i), stop=None, step=None):
                self.set_line(i, value)
            case slice(start=None, stop=int(j), step=None):
                self.set_column(j, value)
            case slice(step=int(_)):
                raise NoStep()
            case _:
                raise TypeError(f"key cannot be typed: {type(key)} (usage mat[i:j])")

    def copy(self) -> "Matrix":
        """
        revoie une copy de la matrice
        :return:
        """
        mat = Matrix(self.columns, self.lines)
        for j in range(self.lines):
            for i in range(self.columns):
                mat[i:j] = self[i:j]
        return mat

    def __copy__(self):
        """
        (a utiliser par copy.copy)
        https://docs.python.org/fr/3/library/copy.html
        """
        return self.copy()

    @staticmethod
    def identity(n: int) -> "Matrix":
        """
        crée une matrice identité
        :param n: matrice de taille n x n
        :return: matrice identité
        """
        mat = Matrix(n, val=0)
        for i in range(n):
            mat[i:i] = 1
        return mat

    def transpose(self) -> None:
        """
        transpose la matrice de la matrice
        """
        for j in range(self.columns):
            for i in range(j, self.lines):
                self[i:j], self[j:i] = self[j:i], self[i:j]

    def add(self, other: "Matrix") -> None:
        """
        ajoute dans la matrice actuelle la matrice other
        :param other: autre matrice a ajouter
        :exception NotCompatible
        """
        if other.lines != self.lines and self.columns != other.columns:
            raise NotCompatible("Size other matrix is not Compatible")

        for j in range(self.columns):
            for i in range(self.lines):
                self[i:j] += other[i:j]

    def __add__(self, other: "Matrix") -> "Matrix":
        """
        pour pouvoir utiliser matA + matB
        :param other: other matrix
        :return:
        """
        if not isinstance(other, Matrix):
            raise TypeError(f"key cannot be typed: {type(other)} (usage matA + matB)")
        res = self.copy()
        res.add(other)
        return res

    def __iadd__(self, other: "Matrix") -> "Matrix":
        """
        pour pouvoir utiliser self += other
        :param other: matrice to add
        :return: self
        """
        if not isinstance(other, Matrix):
            raise TypeError(f"key cannot be typed: {type(other)} (usage matA += matB)")

        self.add(other)
        return self

    def mul_coef(self, k: float) -> None:
        """
        multiliplie la matrice par un coeficient k
        :param k: coeficient utiliser
        """
        for j in range(self.columns):
            for i in range(self.lines):
                self[i:j] *= k

    def mul_mat(self, other: "Matrix") -> Matrix:
        """
        mutiplie 2 matrice entre elle (self * other)

        https://fr.wikipedia.org/wiki/Produit_matriciel

        :param other: 2nd matrice
        :return: matrice du résultat
        :raise: NotCompatible if 2 matrix is not compatible
        """
        if self.columns != other.lines:
            raise NotCompatible("line different of column")

        res = Matrix(self.lines, self.columns, 0)
        for j in range(other.lines):
            for i in range(self.columns):
                for k in range(self.lines):
                    res[i:j] = self[k:i] * other[k:j]
        return res

    def __rmul__(self, other) -> "Matrix":
        """
        implement other * self
        :param other: matrix or
        :return:
        """
        match other:
            case float(k) | int(k):
                # TODO
                ret = self.copy()
                ret.mul_coef(k)
                return ret

            case Matrix():
                # TODO
                return other.mult_mat(self)

            case _:
                raise TypeError(f"key cannot be typed: {type(other)} (usage k * mat or mat1 * mat2)")
