m = int(input("Podaj liczbe wierszy: "))
n = int(input("Podaj liczbe kolumn: "))
tab = [[i * j for j in range(m)] for i in range(n)]
print(tab)