import numpy as np

def get_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input(f"Enter element [{i}][{j}]: "))
            row.append(value)
        matrix.append(row)
    return matrix

def matrix_addition_nested(m1, m2):
    res = [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]
    return res

rows = int(input("Enter num of rows: "))
cols = int(input("Enter num of columns: "))

print("\nEnter elements for Matrix 1:")
matrix1 = get_matrix(rows, cols)
print("\nEnter elements for Matrix 2:")
matrix2 = get_matrix(rows, cols)

result = matrix_addition_nested(matrix1, matrix2)

print("\nResult Matrix :")
for row in result:
    print(row)


def matrix_add_numpy():
    print("\nMatrix addition using numpy: \n")
    mat1 = np.array([[5, 12, 9], [4, 1, 2], [2, 6, 1]])
    mat2 = np.array([[1, 2, 3], [3, 2, 1], [3, 2, 1]])
    mat3 = mat1 + mat2
    print(mat3)

matrix_add_numpy()