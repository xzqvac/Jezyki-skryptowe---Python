import os
import glob
import re

#print(os.getcwd())
pliki = glob.glob("plik_zaszyfrowany**_????????.txt")
print(type(pliki))
#print(os.listdir())
#print(type(pliki[0]))
pattern = "ny(.*?)_"
substring = re.search(pattern, pliki[1]).group(1)
print(substring)
print(pliki[1])