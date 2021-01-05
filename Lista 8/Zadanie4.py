def check_control_number(PESEL):
    a = int(PESEL[0]) * 1
    b = int(PESEL[1]) * 3
    c = int(PESEL[2]) * 7
    d = int(PESEL[3]) * 9
    e = int(PESEL[4]) * 1
    f = int(PESEL[5]) * 3
    g = int(PESEL[6]) * 7
    h = int(PESEL[7]) * 9
    i = int(PESEL[8]) * 1
    j = int(PESEL[9]) * 3
    control_sum = (a + b + c + d + e + f + g + h + i + j) % 10
    last_index = (10 - control_sum) % 10
    if PESEL[10] == str(last_index):
        print("PESEL jest poprawnie zdefiniowany")
        return True
    else:
        return False


def plec(index):
    index = int(index)
    if index % 2 == 0:
        return "Kobieta"
    else:
        return "Mężczyzna"


data = open("PESEL.txt", "r")
save_file = open("Odpowiedzi.txt", "w")
for line in data:
    if check_control_number(line):
        if 1 <= int(line[2:4]) <= 12:
            path = "19" + line[0:2] + "-" + line[2:4] + "-" + line[4:6] + ";" + '\t' + "Plec: " + plec(line[9])
        elif 21 <= int(line[2:4]) <= 32:
            path = "20" + line[0:2] + "-" + str(int(line[2:4]) - 20) + "-" + line[4:6] + ";" + '\t' + "Plec: " + plec(line[9])
        elif 41 <= int(line[2:4]) <= 52:
            path = "21" + line[0:2] + "-" + str(int(line[2:4]) - 40) + "-" + line[4:6] + ";" + '\t' + "Plec: " + plec(line[9])
        elif 61 <= int(line[2:4]) <= 72:
            path = "22" + line[0:2] + "-" + str(int(line[2:4]) - 60) + "-" + line[4:6] + ";" + '\t' + "Plec: " + plec(line[9])
        elif 81 <= int(line[2:4]) <= 92:
            path = "18" + line[0:2] + "-" + str(int(line[2:4]) - 80) + "-" + line[4:6] + ";" + '\t' + "Plec: " + plec(line[9])
        save_file.write('\n' + "nr PESEL: " + line + "Data urodzenia " + path)
    else:
        print("PESEL", line, "nie jest poprawnie zdefiniowany")


