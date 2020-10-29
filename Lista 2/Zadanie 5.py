text = input()
center = int(len(text)//2)
a = "PYTHON"
d = text[:center] + a + text[center:]
print(d)