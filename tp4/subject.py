from .ExceptionMatrix import *
from tools import TODO
"""
Rappelle sur les visibilité en python:
self.a: "public"
self.__a: "private"
https://www.geeksforgeeks.org/private-variables-python/

Nous allons utiliser @property pour faire des getter et des setter
https://www.programiz.com/python-programming/property

Des TODO(n) dans ce fichier sont laisser remplacer les par la bonnes définition
- n = k veux dire que c'est faisable en k instructions
- si n est pas présent alors n = 1
- si n est None aucune indication est donnée sur le nombres d'instructions nécéssaire 
pour ne pas influhencer la réponse
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
        if TODO():
            raise NotNegative("n", n)
        elif TODO():
            m = n
        elif TODO():
            raise NotNegative("m", m)

        # add attributes
        TODO(3)

    @property
    def lines(self) -> int:
        """
        nombre de lignes dans la matrices
        """
        TODO()

    @property
    def columns(self) -> int:
        """
        nombre de colones dans la matrices
        """
        TODO()

    def is_squared(self) -> bool:
        """
        vraie si la matrice est carrée
        """
        TODO()

    @property
    def array_mat(self) -> tuple[tuple[float]]:
        """
        liste de liste d'entier représentant la matrice
        :key est une copie des donnée
        :return donné de la matrice
        """
        # pseudo code:
        # t = []
        # for i=0 to self.lines:
        #   t_line = []
        #   for j=0 to self.columns:
        #       t_line.append(self.data at i j)
        #   t.append(t_line cast to tupple)
        # return t cast to tupple

        # avec un comprehension:
        # return tuple(tuple(val for val in line) for line in self.__data)
        TODO(1)  # 1 avec une comprehension

    @property
    def array_simple(self) -> tuple[float]:
        """
        renvoie une liste simple de notre matrice

        """
        # pseudo code
        # t = []
        # for i=0 to self.lines:
        #   for j=0 to self.columns:
        #       t_line.append(self.data at i j)
        # return t cast to tupple

        # return tuple(x for line in self.__data
        #                for x in line)
        TODO()  # 1 avec une comprehension

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
        TODO()

    def get(self, i: int, j: int) -> float:
        """
        récupère la valeur a la ligne i et a la colonne j
        :param i: ligne
        :param j: colonne
        :return: valeur trouver
        :exception OutOfRange si i ou j n'est pas dans la matrice
        """
        # utiliser les méthode privé précédentes
        TODO(3)

    def __set_without_check(self, i: int, j: int, val: float) -> None:
        """
        methode privé de set qui ne check pas la validité de i et j
        :param i: ligne
        :param j: colonne
        :return: valeur trouver
        """
        # meme idée que __get_without_check mais change la valeur
        TODO()

    def set(self, i: int, j: int, val: int) -> None:
        """
        remplace la valeur a la ligne i et a la colonne j par val
        :param i: ligne
        :param j: colonne
        :param val: valeur a changer
        :exception OutOfRange si i ou j n'est pas dans la matrice
        """
        # meme idée que get mais change la valeur
        TODO(3)

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
        # 1: check si la ligne existe
        # 2: récupérer la ligne
        TODO(2)

    def get_column(self, j: int) -> [int]:
        """
        renvoie la colonne j dans une liste
        :param j: colonne a récupéré
        :return: colonne
        :exception OutOfRange si la colonne j n'est pas dans la matrice
        """
        # meme idée que get_line
        TODO(2)

    def __getitem__(self, key: slice) -> float | list[float]:
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
        if TODO():
            raise NotMatchSize(line, self.columns)

        # check i correct
        TODO()

        for j, val in enumerate(line):
            TODO()

    def set_column(self, j: int, col: [int]) -> None:
        """
        change toute colonne avec les valeur de column
        :param j: ligne a modifier
        :param col: valeurs à utiliser
        :exception NotMatchSize si la longueur de la liste line ne peut pas inséré
        """
        if TODO():
            raise NotMatchSize(col, self.lines)

        TODO()

        for i, val in enumerate(col):
            TODO()

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
        """
        TODO(6)

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
        if TODO():
            raise NotCompatible("Arrays is empty")
        n = TODO()
        m = TODO()
        mat = Matrix(n, m)
        for i, line in enumerate(arrays):
            if TODO():
                raise NotCompatible(f"Arrays line {i} has not length {m}")
            for j, val in enumerate(line):
                mat.__set_without_check(TODO(), TODO(), TODO())
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
        if TODO() is None:
            m = n

        if not arr:
            raise NotCompatible("Arrays is empty")
        elif TODO():
            raise NotCompatible(f"Arrays size not compatible with {n=} {m=}")

        mat = Matrix(n, m)
        for i in range(n):
            for j in range(m):
                r = TODO()
                mat.__set_without_check(i, j, TODO())
        return TODO()

    @staticmethod
    def identity(n: int) -> "Matrix":
        """
        crée une matrice identité
        :param n: matrice de taille n x n
        :return: matrice identité
        """
        TODO(4)

    def transpose(self) -> None:
        """
        transpose la matrice de la matrice
        """

        def swap(i, j) -> None:
            """
            echange les valeur de la matrice des position mat[i:j] vers mat[j:i]
            :param i: indice de la ligne deviens indice colone
            :param j: indice de la colone deviens indice de la ligne
            """
            # essayer d'abord de réfléchir avec ce code pour échanger a et b
            # (penser a une ou plusieur variables temporaraire)
            # a, b = 1, 2
            # print(f"{a=}, {b=}") # a=1, b=2
            # TODO
            # TODO
            # TODO
            # print(f"{a=}, {b=}") # a=2, b=1

            # maitenant esssayer dans notre code réel
            tmp = self.__get_without_check(i, j)
            self.__set_without_check(
                TODO(), TODO(),  # indices
                TODO())  # valeurs
            self.__set_without_check(
                TODO(), TODO(),
                TODO())

            # en python un swap peut etre fait aussi en utilisant les tupples
            # (mais nous utiliserons pas ca ici)
            # a, b = b, a

        for j in range(self.columns):
            for i in range(j, self.lines):
                TODO()

    def add(self, other: "Matrix") -> None:
        """
        ajoute dans la matrice actuelle la matrice other
        :param other: autre matrice a ajouter
        :exception NotCompatible
        """
        if TODO(2):
            raise NotCompatible("Size other matrix is not Compatible")

        for j in range(self.columns):
            for i in range(self.lines):
                TODO(2)

    def __add__(self, other: "Matrix") -> "Matrix":
        """
        pour pouvoir utiliser matA + matB
        :param other: other matrix
        :return:
        """
        if not isinstance(other, Matrix):
            raise TypeError(f"key cannot be typed: {type(other)} (usage matA + matB)")
        # bien penser a voir comment réagis self.add et comment une addition elle fonctionne
        TODO(None)

    def __iadd__(self, other: "Matrix") -> "Matrix":
        """
        pour pouvoir utiliser self += other
        :param other: matrice to add
        :return: self
        """
        if not isinstance(other, Matrix):
            raise TypeError(f"key cannot be typed: {type(other)} (usage matA += matB)")

        # ici on optimise comment est fait un +=
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

        # nous n'optimiseront pas l'espace utiliser pour l'opération
        TODO()

    def mul_coef(self, k: float) -> None:
        """
        multiliplie la matrice par un coeficient k
        :param k: coeficient utiliser
        """
        # s'inspriré de add
        TODO(4)

    def __rmul__(self, other: float | int) -> "Matrix":
        """
        implement other * self
        :param other: scalaire a multiplier
        :return:
        """
        match other:
            case float(k) | int(k):
                # comme add bien penser a au modification des matrices utiliser
                TODO(3)

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
        if TODO():
            raise NotCompatible("line different of column")

        res = Matrix(TODO(), TODO(), 0)
        TODO(4) # ne chercher pas a le faire en 4 instructions
        # indication:
        # - il vous faudra au moins 3 bloucle for
        # - un zip peut etre utile pour simpliser le code
        # - utiliser mat[i:j] ou mat[i:] ou mat[i:j] peut aussi simplifier le code
        #   (ne cherchons pas a désactiver des checks)

        # il faut bien réfléchir sur comment se déroule la multiplication de matrice
        # bonne chance !
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
        if TODO():
            raise NotSquared(mat)

        elif TODO():
            return Matrix.identity(mat.columns)

        TODO(3)
        # question a se poser:
        # a = m * m: modifie m ?

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
