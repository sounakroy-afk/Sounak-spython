import numpy as np
scores=np.array([[80,90,100],[70,85,95]])
print(np.max(scores),np.argmax(scores))
print(np.sum(scores, axis=0))
