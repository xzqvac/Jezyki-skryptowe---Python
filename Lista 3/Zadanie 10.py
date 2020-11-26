lista = []
for i in range(2, 5, 2):
    for j in range(0, 9, 2):
        for k in range(0, 9, 2):
            element = str(i)+str(j)+str(k)
            lista.append(int(element))
lista = list(filter(lambda x: x <= 400, lista))
# filtruje liczby mniejsze badz rowne 400 zapisane w liscie i zwraca dzieki rzutowaniu ponownie na liste
print(len(lista))
print(lista)
