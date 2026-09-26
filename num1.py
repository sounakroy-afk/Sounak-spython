import numpy as np
rng=np.random.default_rng(seed=1)
fruits=np.array(["apple","pineapple","pear","banana","grrapes"])
fruit=rng.choice(fruits, size=(3,2))
print(fruit)
