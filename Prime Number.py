number = input("Enter an integer: ")
number = int(number)

if number < 0:
    print("Negative numbers are always composite")

factors = []
non_factors = []

for element in range(1, number + 1):
    a = number / element
    b = number // element
    if a == b:
        factors.append(element)
    else:
        non_factors.append(element)

print(factors)
#print(non_factors)

if len(factors) == 2:
    print(number ,"is a prime number")
elif len(factors) > 2:
    print(number ,"is a composite number")
elif len(factors) == 1:
    print("1 is neither prime nor composite")
elif len(factors) == 0:
    print("0 is neither prime nor composite")