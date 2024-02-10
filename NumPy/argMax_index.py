
#--The argmax() function is used to find the index of the maximum element in the array arr.


import numpy as np
a = np.array([21,2,-35,-4,5,66,-72,8,9])

b = np.array([[1, 4],#0
              [6, 2],#1
              [3, 5]])#2

print(a.argmax())
print(b.argmax())


print("Column Wise", b.argmax(axis = 0)) #Column Wise [1 2]
print("Row Wise", b.argmax(axis = 1)) #Row Wise [1 0 1]