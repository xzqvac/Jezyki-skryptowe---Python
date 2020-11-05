import re
password = input("Type password: ")
l = re.findall("[a-zA-Z]", password)
n = re.findall("[0-9]", password)
s = re.findall("[$#@]", password)
lt = len(password)
if l:
    print("Spełnia warunek")
else:
    print("Nie zawiera co najmniej 1 litery alfabetu [a − z] oraz [A − Z].")

if n:
    print("Spełnia warunek")
else:
    print("Nie zawiera co najmniej 1 liczby z przedziaªu [0 − 9].")

if s:
    print("Spełnia warunek")
else:
    print("Nie zawiera co najmniej 1 znaku specjalnego ze zbioru [$#@].")

if lt >= 6 and lt <=16:
    print("Spełnia warunek")
else:
    print("Dlugość hasła jest mniejsza niz 6 badz wieksza niz 16.")