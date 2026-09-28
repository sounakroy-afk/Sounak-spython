import pandas as pd
import numpy as np

data = pd.read_csv("billing.csv")
print(data.head())
data_np = np.array(data)
print(data_np)
data_np2 = np.where(data_np)
