import numpy as np


def print_exercise(description, var):
    print('\033[95m' + description + '\033[0m')
    print(var, '\n')


"""
BY DEFAULT THE PRINT LIMIT IS SET TO 3 when threshold is crossed
"""


a = np.arange(6)

b = a.reshape(3, 2)

print_exercise('Two dimensional array', b)

c = np.arange(24)

d = c.reshape(2, 3, 4)

print_exercise('Two 2d arrays', d)

e = np.arange(10000)

print_exercise('Array with elipses', e)

f = e.reshape(100,100)

print_exercise('2d array with elipses', f)

g = e.reshape(10, 10, 100)

print_exercise('Multiple 2d arrays', g)

"""
THE DEFAULT PRINT SETTINGS CAN BE CHANGED
"""

np.set_printoptions(threshold=10)   # Prints everything
