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








