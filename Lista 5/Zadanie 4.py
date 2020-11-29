key = {"a": "y", "e": "i", "i": "o", "o": "a", "y": "e"}
# Dla zamiany klucza i jego wartości tworzone są zagnieżdżonw krotki, rzutowana na listę,a następnie rzutowana na słownik
reversed_key = dict(list((value, key) for key, value in key.items()))
print([(value, key) for key, value in key.items()])

# funkcja szyfruj przyjmuje arguemnt, ktory jest szyfrowany wedlug slownika key. Petla for iteruje po kazdej literze
# podanego wyrazu badz ciagu wyrazow. Gdy litera i w podanym wyrazie znajduje sie w slowniku to do zmiennej zaszyfrowany
# przypisywana jest wartosc podanego klucza. Gdy litera i nie znajduje sie w slowniku jest przepisywana do zmiennej zaszyfrowany

def szyfruj(txt):
    zaszyfrowny = ""
    for i in range(len(txt)):
        txt = txt.lower()
        if txt[i] in key:
            letter = txt[i]
            zaszyfrowny += key.get(letter)
        else:
            zaszyfrowny += txt[i]
    return zaszyfrowny

# funkcja odszyfruj dziala dokladnie tak samo jak funckja szyfruj. Nalezalo jednak uprzednio zamienic
# klucz z jego wartosciami

def deszyfruj(txt):
    odszyfrowany = ""
    for i in range(len(txt)):
        txt = txt.lower()
        if txt[i] in reversed_key:
            letter = txt[i]
            odszyfrowany += reversed_key.get(letter)
        else:
            odszyfrowany += txt[i]
    return odszyfrowany


tekst_do_zaszyfrowania = input("Podaj ciąg do zaszyfrowania:\n")
print("Ciąg zaszyfrowany:\n", szyfruj(tekst_do_zaszyfrowania))
tekst_do_odszyfrowania = input("Podaj ciąg do odszyfrowania:\n")
print("Ciąg zaszyfrowany:\n", deszyfruj(tekst_do_odszyfrowania))
