import numpy as np

arra = np.array([[-1, -3, -5, -7],
                 [-2, 4, 6, 8],
                 [8, 9, 0, 4],
                 [7, 5, 1, 2],
                 [-3, 6, -7, 5]
                 ])

#viva code ,aro kijeno ask korsilo bt remove kore egolo korte bolsilo
ar2=np.array(arra.max(axis=1))
a=ar2[ar2>0].sum()
print(ar2)
print(a)
