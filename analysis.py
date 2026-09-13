import numpy as np

# Reproducible dataset (10 students, 3 subjects)
np.random.seed(10)
scores = np.random.randint(40, 101, size=(10, 3)).astype(float)

# Print initial dataset to check row/col orientation
print("Raw Scores Matrix (Rows=Students, Cols=Math/Physics/Chem):\n", scores)
class_average = np.mean(scores)
print(class_average)
math_mask = scores[:, 0] >= 80
high_math_students = scores[math_mask]
print(high_math_students)
chemistry_marks = scores[:, 1]
print(np.max(chemistry_marks))
print(np.min(chemistry_marks))
