import pandas as pd
import numpy as np
mydata = {'Crop': ['Rice', 'Wheat', 'Barley', 'Maize'],
    'Yield': [1010, 1025.2, 1404.2, 1251.7],
    'cost' : [102, np.nan, 20, 68]}
crops = pd.DataFrame(mydata)
print(crops)
print("isnull")
print(crops.isnull())
print("is not null")
print(crops.notnull())
print("sum of null values")
print(crops.isnull().sum())