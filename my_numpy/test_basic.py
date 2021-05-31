import numpy as np
print(np.__version__)

"""
# Arange Method
array = np.arange(20)
print("Array : ", array)
array = np.arange(10, 30, 5)
print("Array : ", array)
array = np.arange(30, 10, -5)
print("Array : ", array)
"""

"""
# NP array propaties
array = np.arange(20).reshape(2, 4)  # numpy.reshape(array, shape, order = 'C')
max = np.amax(array) # max item from array
unique = np.unique([10, 20, 10, 30, 40, 40])
"""

"""
# Zeros Method
array = np.zeros(10, dtype=int)
array = np.zeros((2, 5), dtype=int)
print("Array : ", array)
"""

"""
# Ones Method
array = np.ones(10, dtype=int)
print("Array : ", array)
array = np.ones((2, 5), dtype=int)
print("Array : ", array)
"""

"""
# Empty Method
array = np.empty(2, dtype=int)
print("Array : ", array, "Lenght : ", len(array))
array = np.empty((2, 4))
print("Array : ", array)
"""

"""
# Array Method
l = [i for i in range(20, 30, 2)]
array = np.array(l)
print("Array : ", array)

# NP Array Info
array = np.array([
    [1,2,3],
    [4,5,6]
])
print("Array : ", array, "\nShape : ", array.shape, "\nSize: ", array.size)
print("Dtype : ", array.dtype)
"""

"""
# Linspace Method
array = np.linspace(10, 20, 50)
print("Array : ", array)
"""

"""
# Math Operations
arr1 = np.array([[4, 7], [2, 6]], dtype = np.float64)
arr2 = np.array([[3, 6], [2, 8]], dtype = np.float64) 
addition = np.add(arr1, arr2)
sum = np.sum(arr1)
sqrt = np.sqrt(arr1)
transpose = arr1.T
"""
