list1 = [1,2,3,4,5,6,7,8]
list2=[3,5,6,1,3,2,4,5]

addlist=list1+list2


list3_dict={}

for digit in addlist:
  if digit in list3_dict:
      list3_dict[digit]=1
  else:
      list3_dict[digit]+=1

list3=list(list3_dict.values())

print(list3)