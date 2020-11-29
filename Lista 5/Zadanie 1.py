numbers = {
    "zero": 0, "jeden": 1, "dwa": 2, "trzy": 3, "cztery": 4, "pięć": 5, "sześć": 6, "siedem": 7, "osiem": 8,
    "dziewięć": 9, "dziesięć": 10, "dwadzieścia": 20, "trzydzieści": 30, "czterdzieści": 40, "pięćdziesiąt": 50,
    "jedenaście": 11, "dwanaście": 12, "trzynaście": 13, "czternaście": 14, "piętnaście": 15, "szesnaście": 16,
    "siedemnaście": 17, "osiemnaście": 18, "dziewiętnaście": 19
}  # Słownik z liczbami. Liczba zapisana słownie to klucz, a liczba zapisana w postaci cyfr to wartość klucza

# Funkcja word_to_number pobiera dwa arguemnty. Jeden jest pozycyjny, drugi domyslny. W przypadku, gdy zostanie
# wprowadzona wartosc arguemnt zmieni swoja wartosc na podana przez uzytkownika. Pierwszy człon liczby jest zawsze.
# Pobierana jest wartosc na podstawie 1 czlonu liczby. Jesli istnieje 2 czlon liczby to dla niego rowniez
# odszukiwana jest wartosc na podstawie klucza jakim jest 2 czlon liczby.


def word_to_number(first_word, second_word=None):
    number_of_second_word = 0
    number_of_first_word = (numbers.get(first_word))
    if second_word:
        number_of_second_word = (numbers.get(second_word))
    print(number_of_first_word + number_of_second_word)


word = input()
splitted_words = word.split()
splitted_words.append('0')
word_to_number(splitted_words[0], splitted_words[1])
