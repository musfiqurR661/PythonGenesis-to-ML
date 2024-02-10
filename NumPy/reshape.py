import numpy as np
# a = np.array([3, -5, 2, -8, 9, 0, 7])
#
# print(a.shape)
#
# a.reshape((1, 7))
# print(a)
# # a.reshape((7, 1))
# # print(a)

a = np.array([3, -5, 2, -8])

print(a.shape)

a_reshap=a.reshape((2, 2))
a_reshapTrans=a.reshape((2, 2)).T
print(a_reshap)
print(a_reshapTrans)