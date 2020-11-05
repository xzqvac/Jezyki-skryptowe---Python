vowels = ('a', 'ą', 'e', 'ę', 'i', 'o', 'u', 'y')
consonant = ('b', 'c', 'ć', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ł', 'm', 'n', 'p', 'r', 's', 't', 'w', 'z', 'ż', 'ź')
letter = input("Podaj litere: ")
letter = letter.lower()
if letter in vowels:
    print("To samogłoska")
else:
    print("To spółgłoska")
