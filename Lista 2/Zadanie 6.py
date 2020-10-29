list = ["Kasia", "Basia", "Marek", "Darek"]
list.append("Józek")
print("Lista po dodaniu Józka", list)
list2 = ["Ania", "Basia"]
list.extend(list2)
print("Lista po rozszerzeniu o inna liste", list)
list.sort()
print("Posortowana lista", list)
print("Czwarty student:", list[3])
for x in list:
    if x == "Basia":
        list.remove("Basia")
        list.remove("Basia")
print("Po usunieciu wszystkich Basi", list)
d = len(list)
print("Ilosc studentow: ", d)
krotka = tuple(list)
print(krotka)

