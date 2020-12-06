def rom2dec(value):
    dec = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    length = len(value)
    if value.count("I") > 3 or value.count("X") > 3 or value.count("C") > 3 or value.count("M") > 3:
        return "Podałeś nieprawidłowy zapis. Zwróć uwagę na maksymalną ilość znaków I, X, C, M"
    for i in range(0, length - 1, 1):
        if value[i] == "V" and value[i + 1] == "V":
            return "Podales nieprawidlowy zapis. Zwróć uwagę, że litera V nie może stać obok L i D i siebie samej"
        elif value[i] == "L" and value[i + 1] == "L":
            return "Podales nieprawidlowy zapis. Zwróć uwagę, że litera L nie może stać obok V i D i siebie samej"
        elif value[i] == "D" and value[i + 1] == "D":
            return "Podales nieprawidlowy zapis. Zwróć uwagę, że litera D nie może stać obok L i V i siebie samej"
    if length >= 3:
        for i in range(length, 2, -1):
            if dec.get(value[i - 1]) > dec.get(value[i - 2]) == dec.get(value[i - 3]):
                return "Podałeś nieprawidłowy zapis. Nie może wystąpić tyle znaków poprzedzających"
    for i in range(0, length - 1, 1):
        if dec.get(value[i + 1]) > dec.get(value[i]):
            if value[i] == "I" and (value[i + 1] == "L" or value[i + 1] == "C" or value[i + 1] == "D" or value[i + 1] == "M"):
                return "Podales nieprawidlowy zapis. Zle zmniejszasz I"
            elif value[i] == "X" and (value[i + 1] == "V" or value[i + 1] == "X" or value[i + 1] == "D" or value[i + 1] == "M"):
                return "Podales nieprawidlowy zapis. Zle zmniejszasz X"
            elif value[i] == "C" and (value[i + 1] != "V" or value[i + 1] != "X" or value[i + 1] != "L" or value[i + 1] != "C"):
                return "Podales nieprawidlowy zapis. Zle zmniejszasz C"
            elif value[i] == "V" or value[i] == "L" or value[i] == "D" or value[i] == "M":
                return "Podales nieprawidlowy zapis. Tymi liczbami nie mozna zmniejszać"
    result = 0
    previous_number = 0
    for i in value[::-1]:
        if dec[i] >= previous_number:
            result += dec[i]
        else:
            result -= dec[i]
        previous_number = dec[i]
    return result


print(rom2dec("III"))
print(rom2dec("IV"))
print(rom2dec("XXIII"))
print(rom2dec("LXIX"))
print(rom2dec("CCXVIII"))
print(rom2dec("DXI"))
print(rom2dec("MCMXCIX"))
