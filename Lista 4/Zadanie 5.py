from itertools import permutations


def createList(n, lista):
    for i in range(0, n, 1):
        element = int(input())
        lista.append(element)


lista1 = []
numberOfElements = int(input("Podaj ilość elementów listy: "))
print("Podaj element listy każdorazowo zatwierdzając ENTEREM")
createList(numberOfElements, lista1)
perm = set(permutations(lista1))
print("Oto wszystkie permutacje podanej listy", perm)

