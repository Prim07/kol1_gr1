from matrix import Matrix

matrix_1 = Matrix(4, 5, 6, 7)
matrix_2 = Matrix(2, 2, 2, 1)

matrix_3a = matrix_1 + matrix_2
matrix_3b = matrix_1.addScalarValue(2)

matrix_4a = matrix_1 * matrix_2
matrix_4b = matrix_1.mulScalarValue(2)

matrix_5a = matrix_1 - matrix_2
matrix_5b = matrix_1.subScalarValue(2)

print(matrix_1)
print(matrix_2)
print("***")
print(matrix_3a)
print(matrix_3b)
print(matrix_4a)
print(matrix_4b)
print(matrix_5a)
print(matrix_5b)
