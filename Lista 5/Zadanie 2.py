dig = {
    0: "", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem",
    8: "osiem", 9: "dziewięć"
}

F = {
    0: "", 11: "jedenaście", 12: "dwanaście", 13: "trzynaście", 14: "czternaście", 15: "piętnaście",
    16: "szesnaście", 17: "siedemnaście", 18: "osiemnaście", 19: "dziewiętnaście", 10: "dziesięć",
    20: "dwadzieścia", 30: "trzydzieści", 40: "czterdzieści", 50: "pięćdziesiąt", 60: "sześćdziesiąt",
    70: "siedemdziesiąt", 80: "osiemdziesiąt", 90: "dziewięćdziesiąt"
}

hundreds = {
    0: "", 100: "sto", 200: "dwieście", 300: "trzysta", 400: "czterysta", 500: "pięćset", 600: "sześćset",
    700: "siedemset", 800: "osiemset", 900: "dziewięćset"
}

thousand = {
    1000: "tysiąc"
}


def numberToWord(number):

    word1 = ""
    word2 = ""
    word3 = ""
    word4 = ""
    length = len(number)

    if length == 4:
        number = int(number)
        if 10 < number % 100 < 20:
            second = number % 100
            word2 = F.get(second)
            third = number % 1000 - second
            word3 = hundreds.get(third)
            fourth = number % 10000 - second - third
            word4 = thousand.get(fourth)
        else:
            first = number % 10
            word1 = dig.get(first)
            second = number % 100 - first
            word2 = F.get(second)
            third = number % 1000 - first - second
            word3 = hundreds.get(third)
            fourth = number % 10000 - first - second - third
            word4 = thousand.get(fourth)
    elif length == 3:
        number = int(number)
        if 10 < number % 100 < 20:
            second = number % 100
            word2 = F.get(second)
            third = number % 1000 - second
            word3 = hundreds.get(third)
        else:
            first = number % 10
            word1 = dig.get(first)
            second = number % 100 - first
            word2 = F.get(second)
            third = number % 1000 - first - second
            word3 = hundreds.get(third)
    elif length == 2:
        number = int(number)
        if number < 20:
            word2 = F.get(number)
        else:
            first = number %10
            word1 = dig.get(first)
            second = number % 100 - first
            word2 = F.get(second)
    elif length == 1:
        number = int(number)
        first = number % 10
        word1 = dig.get(first)
    print(word4, word3, word2, word1)


x = input("Podaj liczbe:")
numberToWord(x)
