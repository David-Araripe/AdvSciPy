# Program to multiply two matrices using nested loops
# I need to improve this code to make it more efficient using numpy

import numpy as np
import time
start_time = time.time()

X = np.random.randint(low=0, high=100, size=(250, 250))
Y = np.random.randint(low=0, high=100, size=(250, 251))

result = np.matmul(X, Y)
print(result.shape)

print("--- %s seconds ---" % (time.time() - start_time))