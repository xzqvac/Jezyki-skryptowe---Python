"""Program sluzy do zaszyfrowania podanego tekstu z pliku. Oparty na szyfrze Cezara"""
from datetime import datetime
import os


def calcualte_key():
    statement = True
    while statement is True:
        try:
            key = int(input("Podaj klucz szyfrujący"))
            if (1 <= key <= 10) is False:
                print("Wybrany klucz znajduje się poza zakresem")
                statement = True
            else:
                return key
        except ValueError:
            print("To nie jest liczba")
        except:
            print("Nieobsługiwany błąd:")


def encrypt():
    """"Szyfrowanie"""
    statement = True
    while statement is True:
        path = input("Podaj sciezke do danych: ")
        if not os.path.exists(path):  # jezeli plik nie istnieje badz nie ma takiej sciezki
            print("Nie ma takiej ścieżki")
        else:
            now = datetime.now()
            year = now.strftime("%Y")
            month = now.strftime("%m")
            day = now.strftime("%d")
            key = calcualte_key()

            save_path = input("Podaj sciezke zapisu: ")

            isExist = os.path.exists(save_path)
            if isExist is False:
                os.makedirs(save_path)
            name_file = "plik_zaszyfrowany" + str(key) + "_" + year + month + day + ".txt"

            if name_file in os.listdir(save_path):
                print("Tak plik juz istnieje. Zmien nazwe badz folder docelowy")
            save_full_path = os.path.join(save_path, name_file)

            data = open(path, "rb")  # otwieramy plik w trybie binarnym
            save_file = open(save_full_path, "wb")

            encrypted_word = []
            for line in data:  # pojedyncza linia to tablica bajtów
                line = line.lower()
                for letter in range(len(line)):  # iterujemy po dlugosci tablicy bajtow, poje
                    # wykluczenie liczb, znakow specjalnych, spacji, znaków interpunkcyjnych
                    if (0 <= line[letter] < 65) or (91 < line[letter] < 97) or (122 < line[letter] <= 127):
                        encrypted_word.append(line[letter])
                    elif 97 <= line[letter] + key <= 122:
                        encrypted_word.append(line[letter] + key)
                    elif line[letter] + key > 122:
                        encrypted_word.append(line[letter] - 26 + key)
            save_file.write(bytes(encrypted_word))
            data.close()
            save_file.close()
            statement = False


encrypt()
