# Numpy operations:
# Sorting
# Merging
# Argument Sorting (find the sorted indices)

#sorting
import numpy as np

arr = np.array([3, 1, 4, 2])
sorted_arr = np.sort(arr)
print("Sorted array:", sorted_arr)
sorted_arr = np.sort(arr)[::-1]  # Reverse the sorted array

print("Des Sortedarray",sorted_arr)

#marge
import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6]])

merged_arr = np.concatenate((arr1, arr2), axis=0)
print("Merged array:", merged_arr)

#column wise
import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6]])

merged_arr = np.concatenate((arr1, arr2.T), axis=1)  # Transpose arr2 to match the number of columns in arr1
print("Merged array:", merged_arr)

# Argument Sorting (find the sorted indices)
import numpy as np

arr = np.array([3, 1, 4, 2])
sorted_indices = np.argsort(arr)
print("Sorted indices:", sorted_indices)
