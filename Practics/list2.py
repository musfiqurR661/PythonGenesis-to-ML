# Example lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Merge both lists into a single list
merged_list = list1 + list2

# Create an empty dictionary to store the counts of each digit
digit_counts = {}

# Iterate over the merged list and count the occurrences of each digit
for digit in merged_list:
    if digit in digit_counts:
        digit_counts[digit] += 1
    else:
        digit_counts[digit] = 1

# Create a new list containing distinct digits using the keys of the dictionary
list3 = list(digit_counts.keys())

print("List 1:", list1)
print("List 2:", list2)
print("Distinct digits list (List 3):", list3)
