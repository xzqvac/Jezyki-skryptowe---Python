import SzyfrCezara


encrypted = input("Podaj tekst do zaszyfowania")
decrypted = input("Podaj tekst zaszyfrowany")

SzyfrCezara.encrypt(encrypted)
SzyfrCezara.decrypt(decrypted)