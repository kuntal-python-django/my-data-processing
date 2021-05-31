import pandas as pd


"""
data = ['Geeks', 'For', 'Geeks', 'is',  'portal', 'for', 'Geeks']
ser = pd.Series(data, index=list(range(1, len(data)+1)))
print(ser)
# print(ser[4])

1     Geeks
2       For
3     Geeks
4        is
5    portal
6       for
7     Geeks
dtype: object
"""


"""
ser = pd.Series(10, index =[0, 1, 2, 3, 4, 5])
print(ser)
"""


"""
d = {'Geeks' : 10, 'for' : 20, 'geeks' : 30}
ser = pd.Series(d)
print(ser)

Geeks    10
for      20
geeks    30
dtype: int64
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
print(data.info()) # print the info about enitre data
print(data.describe())  # print description of entire data
print(data["Salary"].info()) # print the info about Salary column
print(data["Salary"].describe())  # print description about Salary column
data["Salary"] = data["Salary"].astype(int)  # Updating Data Type
data["Number"] = data["Number"].astype(str)  # Updating Data Type
salary_list = data["Salary"].tolist()  # Converting to list
"""
