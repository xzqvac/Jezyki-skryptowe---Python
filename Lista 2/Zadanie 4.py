text = input("Podaj dowolony napis: ")
replacedText = text[0] + text[1:].replace(text[0], "$")
# Pobierany jest znak z lancucha o indeksie zero i nastepnie dodawana jest reszta łańcucha z wykorzystaniem metody
# replace, ktora zamienia kazdy taki sam znak jak ten o indeksie zero na znak dolara
print(replacedText)
