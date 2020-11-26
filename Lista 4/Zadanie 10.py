def NWD(a, b):
    while a != b:
        a, b = max(a, b), min(a, b)
        a = a - b
    return a

a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
print(NWD(a, b))
