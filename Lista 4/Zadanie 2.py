def repeated(n):
    return list(dict.fromkeys(n))
lista1 = repeated([1, 1, 3, 1, 4, 4, 5, 6, 9])
print(lista1)