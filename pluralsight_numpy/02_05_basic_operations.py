import numpy as np


def print_exercise(description, var):
    print('\033[95m' + description + '\033[0m')
    print(var, '\n')


"""
ELEMENTWISE INPUT DIMENSIONS HAVE T BE THE SAME
"""


# Define array to work with
a = np.array([10, 10, 10])
a2 = np.array([10, 10])
b = np.array([5, 5, 5])

A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 5]])


# Elementwise addition
c = a + b
print_exercise('Element wise addition', c)

# Elementwise multiplication
d = a * b
print_exercise('Element wise multiplication', d)

# Elementwise division
e = a / b
print_exercise('Elementwise division', e)

f = a % 3
print_exercise('Modulo: ', f)

g = a < 10
print_exercise('Comparisons: ', g)


# This is element wise
h = A * B
print_exercise('Multiplication 2d arrays: ', h)

# Matrix multiplications
i = A.dot(B)
print_exercise('Matrix Multiplications', i)

"""
FUNCTIONS CAN BE USED TO ANALYSE ALL THE VALUES WITHIN AN ARRAY OR MATRIX
"""

j = i.sum()
print_exercise('Summing up all elements in a matrix: ', j)

k = i.max()
print_exercise('Maximum value', k)

# This can also be done for 2d arrays, so for each columns or rows separately

a1 = np.arange(12).reshape(3, 4)

l = a1.sum(axis=0)
print_exercise('Summed per column', l)

m = a1.sum(axis=1)
print_exercise('Sum per row', m)









