number = int(input("Podaj liczbe: ")) #1 sposob
if number%2==0:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
string = input("Podaj liczbe: ") #2 sposob
l = len(string) - 1
k = string[l]
print(k == "0"or k == "2" or k == "4" or "6" or "8")
print(number%2==0) #3 sposob

while(number%2 == 0): #4 sposob
    print("liczba jest parzysta")
    break
while (number%2 != 0):
    print("liczba jest nieparzysta")
    break
