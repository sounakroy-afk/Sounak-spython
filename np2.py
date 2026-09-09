import numpy as np

# Prices for 3 products across 3 branches
prices = np.array([[12.0, 45.0, 80.0], [15.0, 50.0, 75.0], [10.0, 40.0, 90.0]])
discounted_prices = prices * 0.8
print(discounted_prices)
maximum_price = np.max(prices)
print(maximum_price)
position_of_maximum_price = np.argmax(prices)
print(position_of_maximum_price)
a = prices[:, 2:3]
print(a)
d_price = prices[(prices >= 20) & (prices <= 70)]
print(d_price)
