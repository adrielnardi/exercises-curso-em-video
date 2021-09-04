import array
A = array.array('i', range(10))
print(A)

import numpy as np
np_A = np.asarray(A)
print(np_A)

np_A[4] = 555
print(np_A)
print(A[4])


#output

#array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#[0 1 2 3 4 5 6 7 8 9]
#[  0   1   2   3 555   5   6   7   8   9]
#555
