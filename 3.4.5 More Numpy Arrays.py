import numpy as np

my_array = np.arange(8)
my_array = np.arange(1, 8)
my_array = np.arange(-1, 9.25, 0.5)

print(my_array)
print(type(my_array))

# arrays from lists
from_list = np.array([1, 2, 3], dtype=np.int8) # dont need 64 bits, this line limits to 8
print(type(from_list[0]))

# 2D arrays
from_list = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int8)
array_2d = np.array((np.arange(0,8,2), np.arange(1,8,2)))
array2d = array_2d.reshape((4, 2))

print(array_2d)
print("1D shape:", my_array.shape)
print("2D shape:", array_2d.shape)

# empty arrays
empty_array = np.zeros((2, 2))
empty_array = np.ones((2, 2))
empty_array = np.empty((2, 2)) # empty returns random values

print(empty_array)

eye_array = np.eye(3, k=1)
eye_array[eye_array == 0] = 2
eye_array[eye_array < 2] = 9
eye_array[:2] = 3
eye_array[1:] = 3
eye_array[:, -1] = 4

print(eye_array, "\n")

sorted_array = np.sort(eye_array, axis=0, kind="mergesort") # kind="heapsort" or "quicksort"
print(sorted_array)

#copy arrays
my_view = sorted_array.view()
my_copy = sorted_array.copy()

my_view[:] = 4
print(my_view, "\n")
print(sorted_array)
