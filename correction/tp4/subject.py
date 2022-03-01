from tp4.ExceptionMatrix import *

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
        """
        nombre de lignes dans la matrices
        """
        return self.__m

    @property
    def columns(self):
        """
        nombre de colones dans la matrices
        """
        return self.__n

    def is_squared(self) -> bool:
        """
        vraie si la matrice est carrée
        """
        return self.columns == self.lines

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

    def __get_without_check(self, i: int, j: int) -> float:
        """
        methode privé de récupère qui ne check pas la validité de i et j
        :param i: ligne
        :param j: colonne
        :return: valeur trouver
        """
        return self.__data[i][j]

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

        return self.__get_without_check(i, j)

    def __set_without_check(self, i: int, j: int, val: float) -> None:
        """
        methode privé de set qui ne check pas la validité de i et j
        :param i: ligne
        :param j: colonne
        :return: valeur trouver
        """
        self.__data[i][j] = val

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

        self.__set_without_check(i, j, val)

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
        return [self.__get_without_check(i, j) for j in range(self.columns)]

    def get_column(self, j: int) -> [int]:
        """
        renvoie la colonne j dans une liste
        :param j: colonne a récupéré
        :return: colonne
        :exception OutOfRange si la colonne j n'est pas dans la matrice
        """
        self.__check_column_in_range(j)
        return [self.__get_without_check(i, j) for i in range(self.lines)]

    def __getitem__(self, key: slice) -> float | list[float]:
        """
        pour pouvoir utiliser la notation mat[...]

        mat[i: j] == get(i, j)
        mat[i:] == get_line(i)
        mat[:j] == get_column(j)
        :param key: object slice
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

        for j, val in enumerate(line):
            self.__set_without_check(i, j, val)

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

        for i, val in enumerate(col):
            self.__set_without_check(i, j, val)

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
                val = self.__get_without_check(i, j)
                mat.__set_without_check(i, j, val)
        return mat

    def __copy__(self):
        """
        (a utiliser par copy.copy)
        https://docs.python.org/fr/3/library/copy.html
        """
        return self.copy()

    @staticmethod
    def from_array_mat(arrays: list[list[float]] | tuple[tuple[float]]) -> "Matrix":
        """
        crée une matrice avec un array_matrix
        :param arrays: array_matrix utilisé
        :return: matrix object
        :exception: NotCompatible (si arrays n'as pas une forme de matrice correct)
        """
        if not arrays:
            raise NotCompatible("Arrays is empty")
        n = len(arrays)
        m = len(arrays[0])
        mat = Matrix(n, m)
        for i, line in enumerate(arrays):
            if len(line) != m:
                raise NotCompatible(f"Arrays line {i} has not length {m}")
            for j, val in enumerate(line):
                mat.__set_without_check(i, j, val)
        return mat

    @staticmethod
    def from_array_simple(arr: list[float] | tuple[float], n: int, m: int = None) -> "Matrix":
        """
        créé une matrice avec un simple array (version inverse de "self.arraysimple"
        :param arr: tableau ou prendre les valeurs
        :param n: nombre de lignes
        :param m: nombre de colones (default=None dans ce cas n = m)
        :exception: NotCompatible si la taille de l'array
         ne correspond pas a la taille de la matrice demandé
        :key: la question a se poser ici est comment trouvé r (dans arr) tel que:
            mat[i:j] = arr[r]
        """
        if m is None:
            m = n

        if not arr:
            raise NotCompatible("Arrays is empty")
        elif n * m != len(arr):
            raise NotCompatible(f"Arrays size not compatible with {n=} {m=}")

        #
        mat = Matrix(n, m)
        for i in range(n):
            for j in range(m):
                r = j * n + i
                mat.__set_without_check(i, j, arr[r])
        return mat

    @staticmethod
    def identity(n: int) -> "Matrix":
        """
        crée une matrice identité
        :param n: matrice de taille n x n
        :return: matrice identité
        """
        mat = Matrix(n, val=0)
        for i in range(n):
            mat.__set_without_check(i, i, 1)
        return mat

    def transpose(self) -> None:
        """
        transpose la matrice de la matrice
        """
        def swap(i, j):
            tmp = self.__get_without_check(i, j)
            self.__set_without_check(
                i, j,
                self.__get_without_check(j, i))
            self.__set_without_check(
                j, i,
                tmp)

        for j in range(self.columns):
            for i in range(j, self.lines):
                swap(i, j)

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
                val = self.__get_without_check(i, j) + \
                      other.__get_without_check(i, j)
                self.__set_without_check(i, j, val)

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

    def __sub__(self, other: "Matrix") -> "Matrix":
        """
        pour pourvoir utiliser self - other
        :param other: matrice a soustraire
        :return: soustraction des 2 matrices
        """
        if not isinstance(other, Matrix):
            raise TypeError(f"key cannot be typed: {type(other)} (usage matA += matB)")

        return self + (-1 * other)

    def mul_coef(self, k: float) -> None:
        """
        multiliplie la matrice par un coeficient k
        :param k: coeficient utiliser
        """
        for j in range(self.columns):
            for i in range(self.lines):
                val = self.__get_without_check(i, j) * k
                self.__set_without_check(i, j, val)

    def __rmul__(self, other: float | int) -> "Matrix":
        """
        implement other * self
        :param other: scalaire a multiplier
        :return:
        """
        match other:
            case float(k) | int(k):
                ret = self.copy()
                ret.mul_coef(k)
                return ret

            case _:
                raise TypeError(f"key cannot be typed: {type(other)} (usage k * mat)")

    @staticmethod
    def mul_mat(matA: "Matrix", matB: "Matrix") -> "Matrix":
        """
        mutiplie 2 matrice

        https://fr.wikipedia.org/wiki/Produit_matriciel

        :param matA: 1er matrice
        :param matB: 1er matrice
        :return: matrice du résultat
        :raise: NotCompatible if 2 matrix is not compatible
        """
        if matA.columns != matB.lines:
            raise NotCompatible("line different of column")

        res = Matrix(matB.columns, matA.lines, 0)
        for j in range(res.lines):
            for i in range(res.columns):
                for x1, x2 in zip(matA[i:], matB[:j]):
                    res[i:j] += x1 * x2
        return res

    def __mul__(self, other: "Matrix") -> "Matrix":
        """
        implement  self 8 other
        :param other: matrix
        :return:
        """
        if not isinstance(other, Matrix):
            raise TypeError(f"key cannot be typed: {type(other)} (usage mat1 * mat2)")
        return Matrix.mul_mat(self, other)

    @staticmethod
    def pow(mat: "Matrix", n: int) -> "Matrix":
        """
        fait la matrice puissance n
        (ici nous ne cherchons pas avoir la meilleur optimisation)
        :param mat: matrice a élevé à la puissance
        :param n: puissance (n>=0)
        :return: mat ** n
        :exception: NotSquared: si la matrice n'est pas carrée
        """
        if not mat.is_squared():
            raise NotSquared(mat)

        elif n == 0:
            return Matrix.identity(mat.columns)

        for i in range(n):
            mat *= mat
        return mat

    def __pow__(self, power: int, modulo=None) -> "Matrix":
        """
        pour définir la built-in: pow(mat, power) et mat **
        :param power: puissance a calculter
        :param modulo: (non utilisé)
        :return: matrice
        """
        return Matrix.pow(self, power)

    def __str__(self):
        """
        string representation is string of array mat
        """
        return str(self.array_mat)

    def __repr__(self):
        """
        printing representation with repr
        """
        width = max(map(lambda x: len(str(x)), self.array_simple)) + 2
        res = f"n:{self.lines}, m:{self.columns}\n"
        for line in self.array_mat:
            for val in line:
                res += str(val).center(width)
            res += "\n"
        return res
