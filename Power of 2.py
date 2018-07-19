import math

number = input("Enter a number: ")
number = int(number)
if number < 0:
    print("Entered number is negative. Please try again.")
elif number == 0:
    print("0 is an invalid output since logarithm of 0 cannot be computed")

a = math.log(number, 2)
#print(a)

if a == int(a):
    print("The entered number is a power of 2")
else:
    print("The entered number is not a power of 2")