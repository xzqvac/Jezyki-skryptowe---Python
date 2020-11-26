lista1 = ["Kasia", "Basia", "Marek", "Darek"]
lista1.append("Józek")
print("Lista po dodaniu Józka", lista1)
lista2 = ["Ania", "Basia"]
lista1.extend(lista2)
print("Lista po rozszerzeniu o inna liste", lista1)
lista1.sort()
print("Posortowana lista", lista1)
print("Czwarty student:", lista1[3]) # lista zaczyna indeksowanie od zera
print("Dwóch pierwszych studentów:", lista1[0:2])
for x in lista1: # dla kazdego elementu oznaczonego jako x listy lista
    if x == "Basia": # jezeli porownywany element jest rowny Basia
        lista1.remove("Basia") # metoda remove usunie tylko raz element "Basia"
        lista1.remove("Basia") # usuniecie drugiego elementu "Basia"
print("Po usunieciu wszystkich Basi", lista1)
lengthOfLista1 = len(lista1)
print("Ilosc studentow: ", lengthOfLista1)
krotka = tuple(lista1) # konwersja z listy na krotkę
print(krotka)

