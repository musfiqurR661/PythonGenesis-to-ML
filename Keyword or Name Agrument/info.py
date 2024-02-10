# Keyword/Named Arguments
def printInfo(name, age, cgpa='N/A'):
    print(f'Name: {name}, Age: {age}, CGPA: {cgpa}')


printInfo(age=35, cgpa=3.87, name="Mr.Z")
printInfo(age=35, name="Mr.Z")
#printInfo()

#tupple
t1 = (1,2,3)

print(t1)

x, y, z = t1

print(x, y, z)

print(t1[2])