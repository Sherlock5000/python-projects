fibonacci = [0]
terms = input("Enter number of required terms: ")
terms = int(terms)

for i in range(0, terms):
    if len(fibonacci) == 1:
        fibonacci.append(1)
    a = len(fibonacci) - 1
    if len(fibonacci) > 1:
        fibonacci.append(fibonacci[a] + fibonacci[a -1])

print(fibonacci)
