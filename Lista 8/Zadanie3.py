import random

PESEL = []

for identificator in range(0, 10, 1):
    year = random.randint(1800, 2299)
    month = random.randint(1, 12)
    day = random.randint(1, 31)

    if 1800 <= year <= 1899:
        month += 80
    elif 2000 <= year <= 2099:
        month += 20
    elif 2100 <= year <= 2199:
        month += 40
    elif 2200 <= year <= 2299:
        month += 60

    year = str(year)
    month = str(month)
    day = str(day)

    if int(month) < 10:
        month = "0" + month
    if int(day) < 10:
        day = "0" + day

    seven_index = random.randint(0, 9)
    eight_index = random.randint(0, 9)
    nine_index = random.randint(0, 9)
    ten_index = random.randint(0, 9)

    a = int(year[2]) * 1
    b = int(year[3]) * 3
    c = int(month[0]) * 7
    d = int(month[1]) * 9
    e = int(day[0]) * 1
    f = int(day[1]) * 3
    g = seven_index * 7
    h = eight_index * 9
    i = nine_index * 1
    j = ten_index * 3

    control_sum = (a + b + c + d + e + f + g + h + i + j) % 10
    last_index = 10 - control_sum
    last_index = last_index % 10
    identificator = year[2:] + str(month) + str(day) + str(seven_index) + str(eight_index) + str(nine_index) + str(
        ten_index) + str(last_index)
    #print("Rok", year, "Miesiac", month, "Dzien", day, "7in", seven_index, "8in", eight_index, "9in", nine_index,
         # "10in", ten_index, "Kontrolna", last_index)
    print(identificator)

    PESEL.append(identificator)

data = open("PESEL.txt", "w")
for i in range(len(PESEL)):
    data.write(PESEL[i])

data.close()
