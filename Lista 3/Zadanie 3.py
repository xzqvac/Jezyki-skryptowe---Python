import math
print("Wzor na funkcje kwadratowa ax^2+bx+c")
a = float(input("Podaj współczynnik kierunkowy - a"))
while a == 0.0:  # petla bedzie sie wykonywala dopoki uzytkownik nie poda prawidlowej wartosci (a != 0)
    print("To nie jest funkcja kwadratowa. Wspolczynnik a nie moze wynosic 0")
    a = float(input("Podaj poprawny współczynnik kierunkowy - a"))
b = float(input("Podaj współczynnik linniowy - b"))
c = float(input("Podaj wyraz wolny - c"))

delta = pow(b, 2) - 4 * a * c
if delta > 0:
    x1 = (-b - math.sqrt(delta)) / 2 * a
    x2 = (-b + math.sqrt(delta))/ 2 * a
    print("x1= ", x1, "x2= ", x2)
elif delta == 0:
    x0 = (-b/2*a)
    print("x0 = ", x0)
else:
    print("Brak miejsc zerowych")