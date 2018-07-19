import math

number = input("Enter a number: ")
number = int(number)

if number < 0:
    print("Entered number is negative. Therefore, it is not s square number.")

a = math.sqrt(number)

if a == int(a):
    print("The entered number is a perfect square")
else:
    print("The entered number is not a perfect square")