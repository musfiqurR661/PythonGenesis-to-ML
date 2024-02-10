list_int = [3, 4, 3, 0, 1, 3, 3, 4, 2, 7, 8, 7]

count_dict = {}

for a in list_int:
    if a in count_dict:
        count_dict[a] += 1
    else:
        count_dict[a] = 1

print(count_dict)
