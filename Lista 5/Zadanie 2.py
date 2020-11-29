dig = {
    0: "", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem",
    8: "osiem", 9: "dziewięć"
}

numbers = {
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

# Funkcja number_to_word pobiera arguemnt number jako łańcuch. Następnie w zależności od długości podanej liczby
# obliczane są dla odpowiednich jednostek reszty z dzielenia. Na podstawie reszty z dzielenia definiowana jest wartosc
# klucza zapisana w słowniku. Jezeli ostatnie dwie liczby są z przedziału <11-19> to z uwagi na skladnie jezyka polskiego
# obliczana jest tylko jedna liczba.


def number_to_word(number):

    unit_of_number = ""
    ten_of_number = ""
    hundred_of_number = ""
    thousand_of_number = ""
    length = len(number)

    if length == 4:
        number = int(number)
        if 10 < number % 100 < 20:
            second_dig = number % 100
            ten_of_number = numbers.get(second_dig)
            third_dig = number % 1000 - second_dig
            hundred_of_number = hundreds.get(third_dig)
            fourth_dig = number % 10000 - second_dig - third_dig
            thousand_of_number = thousand.get(fourth_dig)
        else:
            first_dig = number % 10
            unit_of_number = dig.get(first_dig)
            second_dig = number % 100 - first_dig
            ten_of_number = numbers.get(second_dig)
            third_dig = number % 1000 - first_dig - second_dig
            hundred_of_number = hundreds.get(third_dig)
            fourth_dig = number % 10000 - first_dig - second_dig - third_dig
            thousand_of_number = thousand.get(fourth_dig)
    elif length == 3:
        number = int(number)
        if 10 < number % 100 < 20:
            second_dig = number % 100
            ten_of_number = numbers.get(second_dig)
            third_dig = number % 1000 - second_dig
            hundred_of_number = hundreds.get(third_dig)
        else:
            first_dig = number % 10
            unit_of_number = dig.get(first_dig)
            second_dig = number % 100 - first_dig
            ten_of_number = numbers.get(second_dig)
            third_dig = number % 1000 - first_dig - second_dig
            hundred_of_number = hundreds.get(third_dig)
    elif length == 2:
        number = int(number)
        if number < 20:
            ten_of_number = numbers.get(number)
        else:
            first_dig = number % 10
            unit_of_number = dig.get(first_dig)
            second_dig = number % 100 - first_dig
            ten_of_number = numbers.get(second_dig)
    elif length == 1:
        number = int(number)
        first_dig = number % 10
        unit_of_number = dig.get(first_dig)
    print(thousand_of_number, hundred_of_number, ten_of_number, unit_of_number)


x = input("Podaj liczbe:")
number_to_word(x)
