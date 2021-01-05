"""Program sluzy do zaszyfrowania podanego tekstu z pliku. Oparty na szyfrze Cezara"""
from datetime import datetime
import os
import re
import glob


def decrypt():
    """"Deszyfrowanie"""
    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")

    statement = True
    while statement is True:
        try:
            data_path = input("Podaj sciezke do katalogu z plikami")
        except FileNotFoundError:
            print("Nie ma takiej sciezki wariacie")
        else:
            files = glob.glob("plik_zaszyfrowany**_????????.txt")
            for data in files:

                full_path = os.path.join(data_path, data)
                encrypted_file = open(full_path, "rb")
                pattern = "ny(.*?)_"
                key = int(re.search(pattern, data).group(1))
                name_file = "plik_deszyfrowany" + str(key) + "_" + year + month + day + ".txt"
                full_path_save = os.path.join(data_path, name_file)
                decrypted_file = open(full_path_save, "wb")

                decrypted_word = []

                for line in encrypted_file:
                    print(line)
                    line = line.lower()
                    for letter in range(len(line)):
                        if (0 <= line[letter] < 65) or (91 < line[letter] < 97) or (122 < line[letter] <= 127):
                            decrypted_word.append(line[letter])
                        elif 97 <= line[letter] - key <= 122:
                            decrypted_word.append(line[letter] - key)
                        elif line[letter] - key < 97:
                            decrypted_word.append(line[letter] + 26 - key)
                decrypted_file.write(bytes(decrypted_word))
                encrypted_file.close()
                decrypted_file.close()
            statement = False


decrypt()

