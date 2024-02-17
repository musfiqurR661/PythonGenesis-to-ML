lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 1
shift = 4

# Get the element at the ith index
element_to_shift = lst.pop(i)

# Calculate the new index after shifting
new_index = (i + shift) % len(lst)

# Insert the element at the new index
lst.insert(new_index, element_to_shift)

print(lst)
