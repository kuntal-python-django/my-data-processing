import pandas as pd
import numpy as np


"""
data = ['Geeks', 'For', 'Geeks', 'is',  'portal', 'for', 'Geeks']
ser = pd.Series(data, index=list(range(1, len(data)+1)))
print(ser)
print(ser[4])
"""

"""
df = pd.read_csv("nba.csv")  
ser = pd.Series(df['Name'])
print(ser[:10])  # 0 to 9 will print
"""


"""
data = pd.Series([5, 2, 3,7], index=['a', 'b', 'c', 'd'])
data1 = pd.Series([1, 6, 4, 9], index=['a', 'b', 'd', 'f'])
d = data.add(data1, fill_value=0) # Add
d = data.sub(data1, fill_value=0) # Sub
"""


"""
data = pd.read_csv("nba.csv")
data.dropna(inplace = True)
data["Salary"] = data["Salary"].astype(int)  # Updating Data Type
data["Number"] = data["Number"].astype(str)  # Updating Data Type
salary_list = data["Salary"].tolist()  # Converting to list
"""
