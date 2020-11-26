number = int(input("Podaj liczbe: "))  # 1 sposob
if number % 2 == 0:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")


string = input("Podaj liczbe: ")  # 2 sposob z wykorzystaniem dlugosci lancucha.
# Sprawdzana jest cyfra jednosci. Jesli jest to cyfra 0, 2, 4, 6 lub 8 to liczba jest patrzysta
lengthOfString = len(string) - 1
unity = string[lengthOfString]
print(unity == "0" or unity == "2" or unity == "4" or unity == "6" or unity == "8")


print(number % 2 == 0)  # 3 sposob, zwraca wartosc true jesli reszta z dzielenia prez 2 jest rowna 0


while number % 2 == 0:  # 4 sposob
    print("liczba jest parzysta")
    break
while number % 2 != 0:
    print("liczba jest nieparzysta")
    break
