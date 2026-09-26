import numpy as np

a = np.zeros((2, 3, 3))
print(a)
b = np.ones((4, 2, 2), dtype="int32")
print(b)
c = np.full((2, 3), 99)
print(c)
d = np.full_like(a.shape, 4, dtype="float32")
print(d)
np1 = np.random.randint(4, shape=(2, 2))
print(np1)
np2 = np.random.random_sample(a.shape)
print(np2)
