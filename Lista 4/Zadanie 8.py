suma = 0
x = int(input("Podaj n-element szeregu harmonicznego: "))
for i in range(1,x,1):
    suma += 1/i
print(suma)