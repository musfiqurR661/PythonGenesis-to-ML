# int functionname(int x, float y){
#     return 0;
# }

def functionname(x, y):
  return 0

def printHello():
  print('hello')

printHello()

def squarefn(x):
  return x*x

y = squarefn(10)
print(y)

#prime
def isPrime(n):
  for i in range(2, n):
    if n % i == 0:
      return False
  return True


# Take user input for the number to check for primality
number = int(input("Enter a number: "))

# Call the isPrime function with the user input and print the result
print(isPrime(number))
