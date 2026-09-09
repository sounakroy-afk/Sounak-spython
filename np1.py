import numpy as np

scores = np.array([[55, 88, 92, 60], [45, 78, 85, 98]])
mid_tests = scores[:, 1:3]
print(mid_tests)
test_means = np.mean(scores, axis=0)
print(test_means)
failing_scores = scores[scores < 60]
print(failing_scores)
curved_scores = np.where(scores < 60, 60, scores)
print(curved_scores)
print(mid_tests)
