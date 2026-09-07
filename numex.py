import numpy as np
rng=np.random.default_rng(seed=1)
letters= np.array(["A","B","C","D"])
print(rng.integers(low=1, high=10, size=(3,2)))
