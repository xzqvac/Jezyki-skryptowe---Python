word = input("Podaj dowolony napis: ")
newWord = word[:2] + word[-2:]
# Pobierane sa litery od indeksu 0 do 2(wyłącznie) oraz od indeksu -2 do końca
print("Nowe slowo to:", newWord)