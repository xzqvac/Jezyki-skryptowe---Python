import time


def fibrek(liczba):
    if liczba == 0:
        return 0
    if liczba == 1:
        return 1
    else:
        return fibrek(liczba - 2) + fibrek(liczba - 1)


def fibitr(liczba, czasit):
    a = 0
    b = 1
    print(a, end=", ")
    for j in range(0, liczba , 1):
        print(b, end=", ")
        b = b + a
        a = b - a
    return print("Czas operacji: ", czasit - time.process_time())


N = int(input("Podaj N"))
czas = 0
for i in range(0, N+1 , 1):
    print(fibrek(i), end=", ")
    czas += time.process_time()
print(" Czas operacji:", czas)
print('\n')
print(fibitr(N, time.time()))

