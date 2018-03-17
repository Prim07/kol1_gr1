import numpy as np


class MatrixIsNotSquare(Exception):
    pass


class MatricesLengthsAreNotEqual(Exception):
    pass


class Matrix:
    def __init__(self, *vals):
        self.matrix_length = len(vals)

        def is_matrix_square(vals):
            return (self.matrix_length ** (1/2)) % 1 == 0

        if not is_matrix_square(vals):
            raise MatrixIsNotSquare()

        self.matrix = []
        self.row_col_length = int(self.matrix_length ** (1/2))
        for i in range(0, self.row_col_length):
            row = []
            for j in range(0, self.row_col_length):
                row.append(vals[i * self.row_col_length + j])
            self.matrix.append(row)

    @staticmethod
    def validateMatricesLentgths(first_matrix, second_matrix):
        if first_matrix.matrix_length != second_matrix.matrix_length:
            raise MatricesLengthsAreNotEqual()

    def __add__(self, other):
        Matrix.validateMatricesLentgths(self, other)
        summed_matrices = np.add(self.matrix, other.matrix).ravel()
        return Matrix(*summed_matrices)

    def addScalarValue(self, n: int):
        summed_matrices = np.add(self.matrix, n).ravel()
        return Matrix(*summed_matrices)

    def __sub__(self, other):
        Matrix.validateMatricesLentgths(self, other)
        subtracted_matrices = np.subtract(self.matrix, other.matrix).ravel()
        return Matrix(*subtracted_matrices)

    def subScalarValue(self, n: int):
        subtracted_matrices = np.subtract(self.matrix, n).ravel()
        return Matrix(*subtracted_matrices)

    def __mul__(self, other):
        Matrix.validateMatricesLentgths(self, other)
        multiplicated_matrices = np.matmul(self.matrix, other.matrix).ravel()
        return Matrix(*multiplicated_matrices)

    def mulScalarValue(self, n: int):
        multiplicated_matrices = []
        for i in range(0, self.row_col_length):
            for j in range(0, self.row_col_length):
                multiplicated_matrices.append(n * self.matrix[i][j])
        return Matrix(*multiplicated_matrices)

    def __str__(self):
        return str(self.matrix)
