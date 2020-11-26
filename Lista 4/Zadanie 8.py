suma = 0
element = int(input("Podaj n-element szeregu harmonicznego: "))
for i in range(1, element+1, 1):
    suma += 1/i
print(suma)
