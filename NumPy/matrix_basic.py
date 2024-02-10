import numpy as np
a = np.array([21,2,-35,-4,5,66,-72,8,9])

b = np.array([[1, 4],
              [6, 2],
              [3, 5]])

print(a.max())
print(b.max())

print("Column Wise", b.max(axis = 0))
print("Row Wise", b.max(axis = 1))

print("Column Wise", b.min(axis = 0))
print("Row Wise", b.min(axis = 1))

print("Column Wise", b.sum(axis = 0))
print("Row Wise", b.sum(axis = 1))

print("Column Wise", b.mean(axis = 0))
print("Row Wise", b.mean(axis = 1))