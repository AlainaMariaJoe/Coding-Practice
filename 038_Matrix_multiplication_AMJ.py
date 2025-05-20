import numpy as np
def Matrix_mul_nested(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
res = Matrix_mul_nested(A, B)
for row in res:
    print(row) 

def Matrix_mul_numpy1():
    print("\nMultiplication using numpy dot () function\n")
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    C = np.dot(A, B)
    print(C)

Matrix_mul_numpy1()

def Matrix_mul_numpy2():
    print("\nMultiplication using numpy @ operator\n")
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    C = A @ B
    print(C)
Matrix_mul_numpy2()
