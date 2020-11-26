klucz = {"a": "y", "e": "i", "i": "o", "o": "a", "y": "e"}


def szyfruj(txt):
    zaszyfrowny = ""
    for i in range(len(txt)):
        txt = txt.lower()
        if txt[i] in klucz:
            letter = txt[i]
            zaszyfrowny += klucz.get(letter)
        else:
            zaszyfrowny += txt[i]
    return zaszyfrowny

def deszyfruj(txt):
    odszyfrowany = ""



tekst = input("Podaj ciąg do zaszyfrowania:\n")
print("Ciąg zaszyfrowany:\n", szyfruj(tekst))
