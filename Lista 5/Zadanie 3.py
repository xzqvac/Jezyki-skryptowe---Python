def rom2dec(value):
    dec = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    dec_list = list(dec.keys())
    count_i = value.count("I")
    count_x = value.count("X")
    count_c = value.count("C")
    count_m = value.count("M")
    length = len(value)
    if count_c > 3 or count_i > 3 or count_m > 3 or count_x > 3:
        print("Podałeś nieprawidłowy zapis. Zwróć uwagę na maksymalną ilość znaków I, X, C, M")
    for i in range(0, length-1, 1):
        if value[i] == "V" and (value[i + 1] == "D" or value[i + 1] == "D"):
            print("Podales nieprawidlowy zapis. Zwróć uwagę, że litery V, L, D nie mogą stać obok siebie")
            break
        elif value[i] == "L" and (value[i + 1] == "V" or value[i + 1] == "D"):
            print("Podales nieprawidlowy zapis. Zwróć uwagę, że litery V, L, D nie mogą stać obok siebie")
            break
        elif value[i] == "D" and (value[i + 1] == "L" or value[i + 1] == "V"):
            print("Podales nieprawidlowy zapis. Zwróć uwagę, że litery V, L, D nie mogą stać obok siebie")
            break
    for i in range(0, length-1, 1):
        if value[i] == "I" and (value[i + 1] == "I" or value[i + 1] == "L" or value[i + 1] == "C" or value[i + 1] == "D" or value[i + 1] == "M"):
            print("Podałeś nieprawidłowy zapis. Litera I może tylko raz wystąpić gdy liczba jest zmniejszana")
            break
        if value[i] == "X" and (value[i + 1] == "X" or value[i + 1] == "V" or value[i + 1] == "X" or value[i + 1] == "D" or value[i + 1] == "M"):
            print("Podałeś nieprawidłowy zapis. Litera X może tylko raz wystąpić gdy liczba jest zmniejszana")
            break
        if value[i] == "C" and (value[i + 1] == "C" or value[i + 1] == "V" or value[i + 1] == "X" or value[i + 1] == "L" or value[i + 1] == "C"):
            print("Podałeś nieprawidłowy zapis. Litera C może tylko raz wystąpić gdy liczba jest zmniejszana")
            break
    previous_number = 0
    for i in value[::-1]:
        if dec[i] >= previous_number:
            result += dec[i]
        else:
            result -= dec[i]
        previous_number = dec[i]
    return result


print(rom2dec("X"))

