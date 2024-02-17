list1 = [1, 2, 3, 4, 5,8]
list2 = [4, 5, 6, 7, 8]

# Find common digits between list1 and list2
common_digits = set(list1) & set(list2)
# Concatenate both lists
combined_list = list1 + list2

# Create an empty dictionary to store distinct digits
distinct_digits = {}

# Iterate over each digit in the combined list
for digit in combined_list:
    # Check if the digit is not in the dictionary
    if digit not in distinct_digits:
        # Add the digit to the dictionary as a key
        distinct_digits[digit] = True

# Convert the dictionary keys back into a list
list3 = list(distinct_digits.keys())

print("List 1:", list1)
print("List 2:", list2)
print("List 3 (with distinct digits):", list3)
