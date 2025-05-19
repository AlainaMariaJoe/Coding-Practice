import numpy as np
def transpose_nested(matrix):
    transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed

matrix = [[1, 2, 3], [4, 5, 6]]
transposed = transpose_nested(matrix)  

print("Original:")
for row in matrix:
    print(row)

print("Transposed:")
for row in transposed:
    print(row)

def transpose_numpy():
    matrix = np.array([[6, 1, 3], [9, 5, 6]])
    print(f"\nOriginal: \n{matrix}") 
    print(f"\nTransposed: \n{matrix.T}")

transpose_numpy()

