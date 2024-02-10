list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(len(list_1))  # to see the list length
print(list_1[5])  # to see the 2nd index value

list1 = [10, 20, -6, 90, 17]

for i in range(len(list1)):
    print(list1[i], end=' ')

print()
print(list1)

# append
list1 = [10, 20, -5, 9, 0]

list1.append(85)
print("Append: ", list1)

# insert
list1.insert(2, 100)
print("Insert : ", list1)

# remove
list1.remove(9)
print("Remove : ", list1)

# sublist or slicing
list1 = [10, 20, 100, -5, 9, 0, 85]

sublist1 = list1[2:7]  # slicing
print("Slicing :", sublist1)

# list sorting
list1 = [10, 20, 100, -5, 9, 0, 85]

list1.sort()
print("Sorted :", list1) #asccending

list1 = [10, 20, 100, -5, 9, 0, 85]

list1.sort(reverse=True)
print("Sorted :", list1) #descending

#list add/ concate
list1 = [10, 11, -5]
list2 = [5, -6, 1]

print(list1 + list2)

list1 = [10, 11, -5]
list2 = [5, -6, 1]

list1.extend(list2)
print(list1)