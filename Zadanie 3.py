import math
a = float(input("Podaj dlugosc boku A: "))
b = float(input("Podaj dlugosc boku B: "))
k = float(input("Podaj miare kata miedzy bokami A i B: "))
P=(a*b*math.sin(k))/2
print("Pole trojkata:", P)