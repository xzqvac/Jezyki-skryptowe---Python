def repeated(n):
    return list(dict.fromkeys(n))  #konwersja na słownik(gdzie elementy nie mogą się powtarzać), a następnie z powrotem na listę


lista1 = repeated([1, 1, 3, 1, 4, 4, 5, 6, 9])
print(type(lista1))
print(lista1)