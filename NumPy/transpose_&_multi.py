import numpy as np
a = np.array([[1,2,3],
              [4,5,6]])

b = np.array([[1,2,3],
              [4,5,6]])

print(b.T)
print(b.T.shape)
c = np.matmul(a, b.T)
print(" ")
print("Multi=" ,c)