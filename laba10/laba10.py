import numpy as np


def create_arrays():
    zeros_arr = np.zeros(10)
    ones_arr = np.ones(10)
    fives_arr = np.full(10, 5)

    return zeros_arr, ones_arr, fives_arr


zeros, ones, fives = create_arrays()

print("Array of zeros:", zeros)
print("Array of ones:", ones)
print("Array of fives:", fives)
