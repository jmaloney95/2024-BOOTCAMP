# Numpy Tutorial 1

# Importing relevant modules
import numpy as np

# Creating a simple array
array = np.array([1, 2, 3, 4, 5])
print(array)

# Different size dimensions

# Zero dimensional array
zero_dim = np.array(3865235)

one_dim = np.array([1, 2, 3])
print(one_dim)

# Two Dimensional Array
two_dim = np.array([[1, 2, 3], [4, 5, 6]])
print(two_dim)

# Three Dimensional Array
three_dim = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]])
print(three_dim)

# Finding the dimension of a given array
print(two_dim.ndim) # ndim prints the dimension of a given array

# Give an array any dimension that you want
new_array = np.array(18, ndmin=5) # ndmin sets a dimension
print(new_array)