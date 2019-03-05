import numpy as np

# Simple array
array_one = np.array([1, 2, 3])

# Initialized with 0
array_with_0 = np.zeros((3, 4))

# Initialized with 1
array_with_1 = np.ones((4, 2))

# Square matrix with diagnals filles with 1
array_eye = np.eye(3)

# Array with increase
array_of_even = np.arange(2, 20, 2)
array_of_even

# Array with floats
array_of_floats = np.arange(0, 10, 0.7)
array_of_floats

# Initialize and reshape a matrix
array_2 = np.arange(6)
array_reshaped = array_2.reshape(3, 2)
array_reshaped

# Make an array like another
array_like = np.zeros_like(array_reshaped)
print(array_like)