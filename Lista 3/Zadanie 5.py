import re
password = input("Type password: ")
atLeastOneLetter = re.findall("[a-zA-Z]", password)
# Jeżeli zostanie odnaleziona mala lub duza litera alfabetu zostanie zwrocona wartosc true
atLeastOneUnit = re.findall("[0-9]", password)
# Jeżeli zostanie odnaleziona mala lub duza litera alfabetu zostanie zwrocona wartosc true
atLeastOneChar = re.findall("[$#@]", password)
# Jeżeli zostanie odnaleziona mala lub duza litera alfabetu zostanie zwrocona wartosc true
lengthOfPassword = len(password)  # długość wprowadzonego hasła. Przyda się do sprawdzenia warunku wymaganej długości
if atLeastOneLetter:  # jeżel prawda ma zostać wykonana instrukcja
    print("Spełnia warunek")
else:  # W przeciwnym wypadku
    print("Nie zawiera co najmniej 1 litery alfabetu [a − z] oraz [A − Z].")

if atLeastOneUnit:
    print("Spełnia warunek")
else:
    print("Nie zawiera co najmniej 1 liczby z przedziału [0 − 9].")

if atLeastOneChar:
    print("Spełnia warunek")
else:
    print("Nie zawiera co najmniej 1 znaku specjalnego ze zbioru [$#@].")

if 6 <= lengthOfPassword <= 16:
    print("Spełnia warunek")
else:
    print("Dlugość hasła jest mniejsza niz 6 badz wieksza niz 16.")

