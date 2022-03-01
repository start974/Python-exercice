from random import randint

import pytest

# from correction.tp4 import Matrix
from tp4 import Matrix
from tp4.ExceptionMatrix import *


def dot(m1, m2):
    return [
        [sum(x * y for x, y in zip(m1_r, m2_c)) for m2_c in zip(*m2)] for m1_r in m1
    ]


def pow(m, n):
    for i in range(n):
        m = dot(m, m)
    return m


def test_init_error():
    with pytest.raises(NotNegative):
        Matrix(-1, 10)

    with pytest.raises(NotNegative):
        Matrix(1, -1)

    with pytest.raises(NotNegative):
        Matrix(1, 0)


def test_lines_columns():
    mat = Matrix(2, 3)
    assert mat.lines == 3
    assert mat.columns == 2

    mat = Matrix(2)
    assert mat.lines == mat.columns == 2


def test_is_squares():
    assert Matrix(3, 3).is_squared()
    assert Matrix(3).is_squared()
    assert not Matrix(3, 4).is_squared()


def test_arrays():
    assert Matrix(5, 2).array_mat == tuple([tuple([0] * 5)] * 2)
    assert Matrix(5, 2, 10).array_mat == tuple([tuple([10] * 5)] * 2)


def test_simple():
    assert Matrix(5, 2).array_simple == tuple(0 for _ in range(10))
    assert Matrix(5, 2, 10).array_simple == tuple(10 for _ in range(10))


def test_get():
    assert Matrix(2).get(0, 1) == 0
    assert Matrix(2, val=1).get(1, 0) == 1
    assert Matrix(2, val=2)[0:0] == 2


def test_get_error():
    with pytest.raises(OutOfRange):
        Matrix(1, 2).get(-1, 0)

    with pytest.raises(OutOfRange):
        Matrix(1, 2).get(10, 0)


def test_set():
    mat = Matrix(2, 3)
    assert mat.get(0, 1) == 0
    assert mat.get(1, 0) == 0
    mat.set(0, 1, 1)
    mat[1:0] = 2  # same as :mat.set(1, 0, 2)
    assert mat.get(0, 1) == 1, repr(mat)
    assert mat.get(1, 0) == 2, repr(mat)


def test_set_error():
    with pytest.raises(OutOfRange):
        Matrix(1, 2).set(-1, 0, 0)

    with pytest.raises(OutOfRange):
        Matrix(1, 2).set(1, 10, 0)


def test_eq():
    mat22 = Matrix(2)
    mat32 = Matrix(3, 2)
    mat22_copy = Matrix(2)
    mat22_copy[1:0] = 3

    assert mat22 == mat22
    assert mat32 == mat32
    assert mat22 != mat32

    assert mat22 != mat22_copy
    mat22[1:0] = 3
    assert mat22 == mat22_copy


def test_get_line():
    mat = Matrix(2, 3)
    mat[0:0] = 1
    assert mat.get_line(0) == [1, 0]
    assert mat[1:] == [0, 0]


def test_get_line_error():
    with pytest.raises(OutOfRange):
        Matrix(1, 2).get_line(-1)

    with pytest.raises(OutOfRange):
        Matrix(1, 3).get_line(1)


def test_get_col():
    mat = Matrix(2, 3)
    mat[0:1] = 1
    assert mat.get_column(0) == [0, 0, 0]
    assert mat[:1] == [1, 0, 0]


def test_get_column_error():
    with pytest.raises(OutOfRange):
        Matrix(1, 2).get_column(-1)

    with pytest.raises(OutOfRange):
        Matrix(3, 1).get_column(1)


def test_set_line():
    mat = Matrix(2, 3)
    assert mat.get_line(0) == [0, 0]
    mat.set_line(0, [1, 2])
    assert mat[0:] == [1, 2], repr(mat)
    mat[1:] = [4, 4]
    assert mat[1:] == [4, 4], repr(mat)


def test_copy():
    mat = Matrix(2)
    mat_copy = mat.copy()
    assert mat == mat_copy
    mat[1:0] = 3
    assert mat != mat_copy


def test_from_array_mat():
    mat22 = Matrix(2)
    mat22.set(0, 0, 1)
    mat22.set(1, 1, 2)

    mat22Bis = Matrix.from_array_mat(mat22.array_mat)
    assert mat22Bis == mat22


def test_from_array_mat_error():
    with pytest.raises(NotCompatible):
        Matrix.from_array_mat([])

    with pytest.raises(NotCompatible):
        Matrix.from_array_mat([[1, 2], [1]])


def test_from_array_simple():
    mat22 = Matrix(2)
    mat22.set(0, 0, 1)
    mat22.set(1, 1, 2)

    mat22Bis = Matrix.from_array_mat(mat22.array_mat)
    assert mat22Bis == mat22


def test_from_array_simple_error():
    with pytest.raises(NotCompatible):
        Matrix.from_array_simple([], 1)

    with pytest.raises(NotCompatible):
        Matrix.from_array_simple([1, 2, 3, 4], 3)


@pytest.mark.parametrize("n", list(range(1, 6)) + [randint(2, 50) for _ in range(5)])
def test_identity(n):
    expect = Matrix(n, val=0)
    for i in range(n):
        expect[i:i] = 1
    assert Matrix.identity(n) == expect


def test_transpose():
    mat = Matrix(3)
    mat[0:] = [1, 2, 3]

    mat_t = Matrix(3)
    mat_t[:0] = [1, 2, 3]

    mat_copy = mat.copy()
    mat.transpose()

    assert mat != mat_copy
    assert mat == mat_t

    mat_id = Matrix.identity(5)
    mat_id_copy = mat_id.copy()
    mat.transpose()

    assert mat_id == mat_id_copy


def test_add():
    mat = Matrix(3, val=1)
    mat[1:1] = 0

    matB = Matrix(3, val=2)
    matB[1:1] = 0

    matC = Matrix(3, val=3)
    matC[1:1] = 0

    mat.add(matB)
    assert mat == matC


def test_add_op():
    matA = Matrix(3, val=1)
    matA[1:1] = 0
    matA_c = matA.copy()

    matB = Matrix(3, val=2)
    matB[1:1] = 0
    matB_c = matB.copy()

    matC = Matrix(3, val=3)
    matC[1:1] = 0

    assert matA + matB == matC

    assert matA == matA_c
    assert matB == matB_c


def test_iadd_op():
    matA = Matrix(3, val=1)
    matA[1:1] = 0
    matA_c = matA.copy()

    matB = Matrix(3, val=2)
    matB[1:1] = 0
    matB_c = matB.copy()

    matC = Matrix(3, val=3)
    matC[1:1] = 0

    matA += matB

    assert matA == matC
    assert matA != matA_c
    assert matB == matB_c


def test_mul_coef():
    mat = Matrix(3)
    mat[0:] = [1, 2, 3]
    mat[1:] = [4, 5, 6]
    mat[2:] = [7, 8, 9]

    mat_r = Matrix(3)
    mat_r[0:] = [2, 4, 6]
    mat_r[1:] = [8, 10, 12]
    mat_r[2:] = [14, 16, 18]

    mat.mul_coef(2)

    assert mat == mat_r


def test_sub_op():
    matA = Matrix(3, val=1)
    matA[1:1] = 0

    matB = Matrix(3, val=2)
    matB[1:1] = 0
    matB_c = matB.copy()

    matC = Matrix(3, val=3)
    matC[1:1] = 0
    matC_c = matC.copy()

    assert matC - matB == matA

    assert matC == matC_c
    assert matB_c == matB_c


def test_mul_mat_id():
    mat = Matrix(3)

    mat[0:] = [1, 2, 3]
    mat[1:] = [4, 5, 6]
    mat[2:] = [7, 8, 9]

    id = Matrix.identity(3)
    assert Matrix.mul_mat(id, mat) == mat
    assert Matrix.mul_mat(mat, id) == mat


def test_mul_mat_square():
    mat = Matrix(3)

    mat[0:] = [1, 2, 3]
    mat[1:] = [4, 5, 6]
    mat[2:] = [7, 8, 9]

    mat_arr = mat.array_mat
    res = Matrix.from_array_mat(dot(mat_arr, mat_arr))

    assert Matrix.mul_mat(mat, mat) == res


def test_mul_op():
    mat = Matrix(3)

    mat[0:] = [1, 2, 3]
    mat[1:] = [4, 5, 6]
    mat[2:] = [7, 8, 9]

    mat_c = mat.copy()

    mat_r = Matrix(3)
    mat_r[0:] = [2, 4, 6]
    mat_r[1:] = [8, 10, 12]
    mat_r[2:] = [14, 16, 18]

    assert 2 * mat == mat_r
    assert mat == mat_c

    mat_mul = Matrix.from_array_mat(dot(mat.array_mat, mat_r.array_mat))
    assert mat * mat_r == mat_mul
    assert mat == mat_c
    assert mat_r == 2 * mat

    mat *= mat_r
    assert mat == mat_mul


def test_mat_pow_id():
    mat_id = Matrix.identity(5)
    assert Matrix.pow(mat_id, 5) == mat_id
    assert Matrix.pow(Matrix(3), 0) == Matrix.identity(3)


@pytest.mark.parametrize("n", (2, 4, 5, 10))
def test_mat_pow(n):
    mat = Matrix(3)
    mat[0:] = [1, 2, 3]
    mat[1:] = [4, 5, 6]
    mat[2:] = [7, 8, 9]

    mat_c = mat.copy()

    res = Matrix.from_array_mat(pow(mat.array_mat, n))
    assert Matrix.pow(mat, n) == res
    assert mat == mat_c


def test_mat_pow_op():
    mat = Matrix(3)
    mat[0:] = [1, 2, 3]
    mat[1:] = [4, 5, 6]
    mat[2:] = [7, 8, 9]

    N = 3
    mat_c = mat.copy()

    res = Matrix.from_array_mat(pow(mat.array_mat, N))
    assert mat ** N == res
    assert mat == mat_c
