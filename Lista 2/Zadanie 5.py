text = input("Podaj dowolny napis")
center = int(len(text)//2)
# wyznaczenie srodka przy pomocy dzielnia całkowitego
addedWord = "PYTHON"
newWord = text[:center] + addedWord + text[center:]
# Polaczenie trzech lancuchow w jeden. Text[:center] oznacza indeks od elementu 0 do obliczonej liczby center - 1(czyli wyłacznie)
# text[center:] oznacza indeksy od obliczonej wartosci center wlacznie do konca lancucha text
print(newWord)