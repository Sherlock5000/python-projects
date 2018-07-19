import random

for num in range(1):
    number = random.randint(1, 101)

entered_number = input("Guess a number:")
entered_number = int(entered_number)

if entered_number > number:
    print("You were off by ", entered_number - number)
    print("The random number generated was ", number)
elif entered_number < number:
    print("You were off by ", entered_number - number)
    print("The random number generated was ", number)
elif entered_number == number:
    print("You vahve guessed correctly !!. The number is indeed ", entered_number)
else:
    print("Input has been given incorrectly. Please try again.")