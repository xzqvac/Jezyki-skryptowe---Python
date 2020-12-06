"""Program sluzy do zaszyfrowania oraz odszyfrowania podanego tekstu. Oparty na szyfrze Cezara"""


#print("Jestem", __name__)

  # klucz szyfrujący i deszyfrujący

def calcualte_key():
    key = int(input("Podaj klucz szyfrujący/deszyfrujący"))
    if key > 26:
        key = key % 26
    return key

def encrypt(txt):
    """"Szyfrowanie"""
    key = calcualte_key()
    encrypted_word = ""
    txt = txt.lower()
    for i in range(len(txt)):
        # wykluczenie liczb, znakow specjalnych, spacji, znaków interpunkcyjnych
        if (0 <= ord(txt[i]) < 65) or (91 < ord(txt[i]) < 97) or (122 < ord(txt[i]) <= 127):
            encrypted_word += txt[i]
        elif 97 <= ord(txt[i]) + key <= 122:
            encrypted_word += chr(ord(txt[i]) + key)
        elif ord(txt[i]) + key > 122:
            encrypted_word += chr(ord(txt[i]) + key - 26)
    print(encrypted_word)


def decrypt(txt):
    """"Deszyfrowanie"""
    key = calcualte_key()
    decrypted_word = ""
    txt = txt.lower()
    for i in range(len(txt)):
        # wykluczenie liczb, znakow specjalnych, spacji, znaków interpunkcyjnych
        if (0 <= ord(txt[i]) < 65) or (91 < ord(txt[i]) < 97) or (122 < ord(txt[i]) <= 127):
            decrypted_word += txt[i]
        elif 97 <= ord(txt[i]) - key <= 122:
            decrypted_word += chr(ord(txt[i]) - key)
        elif ord(txt[i]) - key < 97:
            decrypted_word += chr(ord(txt[i]) + 26 - key)
    print(decrypted_word)


if __name__ == '__main__':
    encrypt("radek9 99zzz !@#$%^&*")
    decrypt("sbefl9 99aaa !@#$%^&*")
