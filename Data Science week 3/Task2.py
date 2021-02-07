import numpy as np

a = np.reshape(np.arange(9), (3,3)) # create a 4x4 array of integers
print(a)
large_values = (a > 5) # test which elements of a are greated than 5
print(large_values)