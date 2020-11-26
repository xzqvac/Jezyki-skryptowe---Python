a = input("Podaj pierwszą liczbę całkowitą: ")
b = input("Podaj drugą liczbę całkowitą: ")
suma = a + b
print(suma)
print("Spodziewałem się innego wyniku.Wczytane liczby zostały wczytane jako typ łańcuch. " 
      "Aby otrzymać wartość równania matematycznego a nie napisu należy dokonać konwersji (rzutowania) na typ int - całkowity")
a = int(a)
b = int(b)
suma = a + b
print(suma)
