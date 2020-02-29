# Here we are going to calculate the variance of a multidimensional array

import numpy as np

data = np.array([
[0,1,2,3,4,5,6,7,8,9],
[2,3,2,3,4,5,6,7,6,7],
[2,3,2,3,4,5,6,7,8,9],
[2,3,2,3,2,3,2,3,2,3],
[3,4,5,4,5,6,7,7,8,8],
[1,1,1,1,1,1,1,1,1,1],
[5,5,6,6,7,7,8,8,9,9],
[1,1,2,2,3,3,4,4,5,5]
])
for d in data:
    print('Array: ', d)
    print('Mean: ', d.mean())
    print('Deviation: ', np.std(d))
    print('Variance: ', np.var(d))
    print('mean of each column: ', np.mean(axis=0))
    print(' ')