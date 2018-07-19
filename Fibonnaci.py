fibonnaci = [0]
terms = input("Enter number of required terms: ")
terms = int(terms)

for i in range(0, terms):
    if len(fibonnaci) == 1:
        fibonnaci.append(1)
    a = len(fibonnaci) - 1
    if len(fibonnaci) > 1:
        fibonnaci.append(fibonnaci[a] + fibonnaci[a -1])

print(fibonnaci)
