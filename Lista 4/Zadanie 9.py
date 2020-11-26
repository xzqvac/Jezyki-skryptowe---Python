wynik = 1
N = int(input("Podaj liczbe calkowita N: "))
if N<0:
    print("Silnia występuje tylko dla liczb naturalnych dodatnich")
i = N
for i in range(N, 1, -1):
    wynik *= i
print(N, '! =', wynik)
