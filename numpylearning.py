import numpy as np

array=np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]])
print(array[1:3])
print(array.ndim)
print(array.shape)
print(len(array.shape) == array.ndim)
print(array[0:4:2])
print(array[:, 0])
print(array[:, 1:4])
print(array[0:2,0:2])
