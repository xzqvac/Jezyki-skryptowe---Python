m = int(input("Podaj liczbe wierszy: "))  # konwersja z typu łańcuch na typ całkowity
n = int(input("Podaj liczbe kolumn: "))
tab = [[i * j for j in range(1, m+1)] for i in range(1, n+1)]  # zagniezdzone petle.
# wewnetrza petla for wykonuje sie dla wierszy i oblicza ona liczbe i*j w zaleznosci od numeru kolumny i wiersza.
# Wewnetrzna petla for wykonuje sie dla zadanej ilosci kolumn.
print(tab)
