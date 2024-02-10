# if-else statment

x = 4

# if(condition){
# }

if x % 2 == 0:
    print("even")
else:
    print('odd')
print("outside if-else")

x = -7

if x > 0:
    print('positive')
elif x == 0:
    print('zero')
else:
    print('negative')
##
x = 15

if 10 < x and x < 20:
    print(f'{x} is between 10 and 20')

if 10 < x < 20:
    print(f'{x} is between 10 and 20')

if x < 10 or x > 20:
    print(f"{x} is not between 10 and 20")
