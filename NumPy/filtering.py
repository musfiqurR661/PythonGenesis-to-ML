import numpy as np
a = np.array([3, -5, 2, -8, 9, 0, 7])

print("a", a)

print("a[[True, False, False, True, True, False, True]]", a[[True, False, False, True, True, False, True]])

print("a>5", a>5)

print("a[a>5]", a[a>5])
print("a[a<2]", a[a<2])