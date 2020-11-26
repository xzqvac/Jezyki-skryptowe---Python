lista1 = [1, 2, 3, 4, 5, 7]
lengthOfLista1 = len(lista1)
suma = 0
iloczyn = 1
for i in range(0, lengthOfLista1, 1):  # petla ma iterowac co jeden od 0 do liczby jaką jest dlugosc listy
    suma += lista1[i]  # rownoznaczne z suma = suma + lista1[i]. Dodaje elementy listy zgodnie z kolejnymi indeksami
    iloczyn *= lista1[i]
print("Suma elementow listy wynosi: ", suma)
print("Iloczyn elementow listy wynosi: ", iloczyn)
