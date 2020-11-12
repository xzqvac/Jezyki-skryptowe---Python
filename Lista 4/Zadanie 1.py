lista1 = [1, 2, 3, 4, 5, 7]
dl = len(lista1)
suma = 0
iloczyn = 1
for i in range(0, dl, 1):
    suma += lista1[i]
    iloczyn *= lista1[i]
print("Suma elementow listy wynosi: ",suma)
print("Iloczyn elementow listy wynosi: ",iloczyn)