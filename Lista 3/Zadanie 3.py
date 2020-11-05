import math
print("Wzor na funkcje kwadratowa ax^2+bx+c")
a = float("Podaj współczynnik kierunkowy")
if a == 0:
    print("To nie jest funkcja kwadratowa")
b = float(input("Podaj współczynnik linniowy"))
c = float(input("Podaj wyraz wolny"))

delta = pow(b,2)-4*a*c
if delta > 0:
    x1 = (-b - math.sqrt(delta))/2*a
    x2 = (-b + math.sqrt(delta))/2*a
    print("x1= ", x1, "x2= ", x2)
elif delta == 0:
    x0 = (-b/2*a)
    print("x0= ")
else:
    print("Brak miejsc zerowych")