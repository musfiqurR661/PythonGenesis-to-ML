#Find out the sum of all corresponding pairs between two numpy arrays if multiplication of the pair is positive
# sum(3*3 + -5*-5 + 0*5)
import numpy as np
a = np.array([3, -5, 2, 9, 0, 7])
b = np.array([3, -5, -2, -1, 5, -1])

positive_index=np.where(a*b > 0)

positiveP_a=a[positive_index]
positiveP_b=b[positive_index]

sumOf_pair=np.sum(positiveP_a*positiveP_b)

print(sumOf_pair)
