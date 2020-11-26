vowels = ('a', 'ą', 'e', 'ę', 'i', 'o', 'u', 'y')
consonant = ('b', 'c', 'ć', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ł', 'm', 'n', 'p', 'r', 's', 't', 'w', 'z', 'ż', 'ź')
letter = input("Podaj litere: ")
lowLetter = letter.lower()  # zapobiegniecie wysypaniu sie programu, gdy uzytkownik poda wielka litere
if lowLetter in vowels:  # jezeli podana litera znaduje sie w liscie vowels
    print("To samogłoska")
else:   # jezeli podana litera nie znajduje sie w liscie vowels
    print("To spółgłoska")



