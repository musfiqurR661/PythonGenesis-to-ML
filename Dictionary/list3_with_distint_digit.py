list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [3, 5, 6, 1, 3, 2, 4, 5]

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

# Create a new list containing the counts of each digit
list3 = list(digit_counts.keys())

print(list3)

#list(digit_counts.values()) gives you a list of the counts of each digit.
#list(digit_counts.keys()) gives you a list of the digits themselves.