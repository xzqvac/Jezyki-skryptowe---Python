wynik =1
N = int(input("Podaj liczbe N: "))
i = N
for i in range(N, i>1, -1):
    wynik *= i
print("N! =", wynik)