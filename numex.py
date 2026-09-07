import numpy as np
ages=np.array([12,18,25,15,40,65,10])
above18=np.where(ages>=18, ages, 0)
print(above18)
