lista1 = [*range(0, 100, 3)] # nastepuje rozpakowanie wszystkich elementow
print(lista1)
del(lista1[5:len(lista1):3])
# nastepuje usuniecie co trzeciego elementu(za co trzeci element odpowiedzialny jest argument k [i:j:k]
#
print(lista1)
average = float((sum(lista1)/len(lista1)))  # zamiast sum mozna uzyc rowniez
print("Srednia", average)
