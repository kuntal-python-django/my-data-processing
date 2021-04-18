import pandas as pd 


"""
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
df = pd.DataFrame(data)
df["Name"] = df["Name"].str.lower() # Lowercasing
df["Name"] = df["Name"].str.upper() # Uppercasing
data["Team"] = data["Team"].str.split("t", n = 1, expand = True) # split
# substring to be searched
sub = 'a'
data["Indexes"] = data["Name"].str.find(sub) # Find
# string to be searched for
search ='r'
data["Findall(name)"]= data["Name"].str.findall(search)
data["bool_series"]= data["College"].str.isalpha() # all characters in each string in series are alphabetic(a-z/A-Z)
data["Name Length"]= data["Name"].str.len() # len function
"""


"""
# Read CSV
df = pd.read_csv("pokemon.csv")
pd.read_csv("pokemon.csv", header=[1, 2])
df = pd.read_csv("pokemon.csv", skiprows = [1, 2, 3, 4])
df = pd.read_csv("pokemon.csv", usecols=["Type"])
print(df)
"""


"""
# Create CSV
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
# df = pd.DataFrame(data)
# df = pd.DataFrame(data, columns=['Full Name', 'Age', 'Address', 'Qualification'])
df = pd.DataFrame(data, index=list(range(1, 5)))
# df.to_csv('file.csv')
df.to_csv('file2.csv', header=False, index=False)
"""


"""
# Adding new column to existing DataFrame
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Height': [5.1, 6.2, 5.1, 5.2],
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc']}
df = pd.DataFrame(data)

# adding column
df.insert(2, "Age", [21, 23, 24, 21], True)
address = ['Delhi', 'Bangalore', 'Chennai', 'Patna']
df['Address'] = address

# dropping passed columns
df.drop(["Team", "Weight"], axis = 1, inplace = True)

print(df)
"""


"""
# Group By
data = {'Name':['Jai', 'Anuj', 'Jai', 'Princi', 
                 'Gaurav', 'Anuj', 'Princi', 'Abhi'], 
        'Age':[27, 24, 22, 32, 
               33, 36, 27, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
                   'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd',
                         'B.Tech', 'B.com', 'Msc', 'MA']}
df = pd.DataFrame(data)

group_by_column = df.groupby('Name')
group_by_column = df.groupby(['Name', 'Qualification'])
print(group_by_column.groups)
"""


# Joining
# data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
#         'Age':[27, 24, 22, 32], 
#         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
#         'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 
# df1 = pd.DataFrame(data1,index=[0, 1, 2, 3])
# data2 = {'Name':['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'], 
#         'Age':[17, 14, 12, 52], 
#         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
#         'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']}
# df2 = pd.DataFrame(data2, index=[4, 5, 6, 7])
# res = pd.concat([df1, df2])
# print(res)


# data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
#         'Age':[27, 24, 22, 32], 
#         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
#         'Qualification':['Msc', 'MA', 'MCA', 'Phd'],
#         'Mobile No': [97, 91, 58, 76]} 
# df1 = pd.DataFrame(data1,index=[0, 1, 2, 3])
# data2 = {'Name':['Gaurav', 'Anuj', 'Dhiraj', 'Hitesh'], 
#         'Age':[22, 32, 12, 52], 
#         'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'], 
#         'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons'],
#         'Salary':[1000, 2000, 3000, 4000]}
# df2 = pd.DataFrame(data2, index=[2, 3, 6, 7]) 
# res = pd.concat([df1, df2], axis=1, join='inner')
# print(res)
