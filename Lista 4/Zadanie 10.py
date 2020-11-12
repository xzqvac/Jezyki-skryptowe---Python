def nwd(a, b):
    while(a!=b):
        if(a>b):
            a -= b
        else:
            b -= a
    return a
print("Podaj 1 liczbe calkowita")
x = int(input())
print("Podaj 2 liczbe calkowita")
y = int(input())
print(nwd(x,y))