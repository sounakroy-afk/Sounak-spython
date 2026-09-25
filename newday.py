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
print(A[2, 2])
print(A[2:
