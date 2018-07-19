import math

number1 = input("Enter first number: ")
number2 = input("Enter second number: ")
number1 = int(number1)
number2 = int(number2)

if number1 == 0 and number2 == 0:
    print("0 cannot be passed as input")

a = math.log(number1, number2)
b = math.log(number2, number1)

if number1 > number2:
    if a == int(a):
        print(number1, "is a power of", number2)
if number1 < number2:
    if b == int(b):
        print(number2, "is a power of", number1)