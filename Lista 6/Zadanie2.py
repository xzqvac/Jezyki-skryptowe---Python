KLUCZ = 3


def szyfruj(txt):
    zaszyfrowny = ""
    txt = txt.lower()
    print(txt)
    for i in range(len(txt)):
        if ord(txt[i]) > 122 - KLUCZ:
            zaszyfrowny += chr(ord(txt[i]) + KLUCZ - 26)
        else:
            zaszyfrowny += chr(ord(txt[i]) + KLUCZ)
    return zaszyfrowny


tekst = input("Podaj ciąg do zaszyfrowania:\n")
print("Ciąg zaszyfrowany:\n", szyfruj(tekst))