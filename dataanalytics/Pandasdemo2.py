"""
program - Pandasdemo2.py
Pandas - DataFrame,Series
Series - timeseries
"""
import pandas as pd
print("create a series")
runs=[20,21,18,16,15]
runsseries = pd.Series(runs)
print(runsseries)
print("data type of series ",type(runsseries))
print("shape ",runsseries.shape)
print("create a data frame")
topeconomydict ={"Country":["USA","China","Germany","Japan","India"],
                 "GDP":[27,18,4.7,4.2,3.1],
                 "PerCapita":[85,13,56,34,2]}
top5economy = pd.DataFrame(topeconomydict)
print("data type of top5economy ",type(top5economy))
print(top5economy)
print("shape ",top5economy.shape)




