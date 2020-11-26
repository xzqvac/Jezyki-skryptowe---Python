def Fibonacci(n):
    if n <= 0:
        print("Zla liczba")
    elif n == 1:  # wartosc ciagu Fibbonaciego dla liczby 1 wynosi 0
        return 0
    elif n == 2:
        return 1  # wartosc ciagu Fibbonaciego dla liczby 2 wynosi 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)   # rekurencja


p = int(input("Podaj liczbe N"))
print(Fibonacci(p))

