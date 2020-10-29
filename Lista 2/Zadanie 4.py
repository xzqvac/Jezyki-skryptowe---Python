text = input()
x = text[0] + text[1:].replace(text[0],"$")
print(x)