import numpy as np

array1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(array1.shape)
print(array1.ndim)
print(array1.dtype)
print(array1.nbytes)
array1 = np.arange(1, 13, dtype="int16").reshape(3, 4)
print(array1)


A = np.array(
    [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
)
sub_matrix = A[1:3, 1:3]
print(sub_matrix)
co14 = A[:4, 4]
print(co14)
A_mod = A.copy()
A[1:4, 1:4] = 0
print(A)


I = np.identity(3)
print(I)
I = np.full((4, 4), 7)
print(I)
I = np.random.rand(3, 3)
print(I)
I = np.random.randint(1, 10, size=(3, 3))
print(I)

I = np.full((5, 5), 1)
print(I)
B = np.zeros((3, 3))
B[1, 1] = 9
print(B)
I[1:4, 1:4] = B
print(I)


X = np.array([[1, 2], [3, 4]])
Y = np.array([[5, 6], [7, 8]])

print(X * Y)
print(X @ Y)
print(np.linalg.det(X))
print(np.linalg.det(Y))
print(np.sum(X, axis=0))
print(np.sum(X, axis=0))
