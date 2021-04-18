
import pandas as pd
import numpy as np

"""
data = ['Geeks', 'For', 'Geeks', 'is',  'portal', 'for', 'Geeks']
df = pd.DataFrame(data)
df = pd.DataFrame(data, columns=['Heading'], index=list(range(1, len(data)+1)))
print(df)

        0
0   Geeks
1     For
2   Geeks
3      is
4  portal
5     for
6   Geeks

 Heading
1   Geeks
2     For
3   Geeks
4      is
5  portal
6     for
7   Geeks
"""


"""
data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18]}
df = pd.DataFrame(data)
print(df)

    Name  Age
0    Tom   20
1   nick   21
2  krish   19
3   jack   18
"""


"""
data = [['tom', 10], ['nick', 15], ['juli']]
df = pd.DataFrame(data)
print(df)

      0     1
0   tom  10.0
1  nick  15.0
2  juli   NaN
"""


"""
data = [['tom', 10], ['nick', 15], ['juli', 14]]
df = pd.DataFrame(data, columns = ['Name', 'Age'], index=['a', 'b', 'c'])
print(df)

   Name  Age
a   tom   10
b  nick   15
c  juli   14
"""


"""
data = [{'a': 1, 'b': 2}, {'a':10, 'c': 20, 'd': 30}]
df = pd.DataFrame(data)
print(df)

    a    b     c     d
0   1  2.0   NaN   NaN
1  10  NaN  20.0  30.0
"""


"""
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
df = pd.DataFrame(data)
print(df)
print(df[['Name', 'Qualification']]) # to print only two column

     Name  Age    Address Qualification
0     Jai   27      Delhi           Msc
1  Princi   24     Kanpur            MA
2  Gaurav   22  Allahabad           MCA
3    Anuj   32    Kannauj           Phd
"""


"""
# To read csv file and operation
data = pd.read_csv("nba.csv")
print(data.to_string())  # to print the entire data By default, when you print a DataFrame, you will only get the first 5 rows, and the last 5 rows
print(data.loc[0]) # row 0 will print
print(data.loc[0: 5]) # row 0 to 5 will print
print(data.info()) # print the info about enitre data
print(data.describe())  # print description of enitre data
print(data["Age"])  # print the "Age" column only
"""


"""
# Working with data Missing data
df = pd.read_csv('data.csv')
df.dropna(inplace=True) # By default, the dropna() method returns a new DataFrame, and will not change the original.
df.fillna(130, inplace = True)  # fill the nan value with 130 for all
df["Calories"].fillna(130, inplace = True)  # only Calories column nan value will fill with 130
df["Calories"].fillna(df["Calories"].mean(), inplace = True)     # Mean
df["Calories"].fillna(df["Calories"].median(), inplace = True)   # Median
df["Calories"].fillna(df["Calories"].mode()[0], inplace = True)  # Mode
"""


"""
dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}
df = pd.DataFrame(dict)
for i, j in df.iterrows():
    print(i, j)  # i-->Index j-->Each row data
"""


"""
# Special Method
df = pd.read_csv("employees.csv")
df.dropna(inplace = True)
hightest_5_salary = df.nlargest(5, "Salary")
smallest_5_salary = df.nsmallest(5, "Salary")
df.sort_values("Salary", ascending=True, inplace=True)
print(df.head(10))
"""
