i = int(input("Podaj zmienna i: "))  # konwersja z łańcucha na typ całkowity
j = [x * i for x in range(1, 11)]  # zdefiniowanie j jako listy, ktorej elementami sa wyniki mnozenia i*j
print(j)
