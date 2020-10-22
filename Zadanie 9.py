import cmath
z = complex(float(input("Podaj czesc rzeczywista: ")), float(input("Podaj część urojoną: ")))
print ("Część rzeczywista : ", z.real)
print ("Część urojona : ", z.imag)
modul = (z.real + z.imag)**(1/2)
print("Modul jest rowny:", modul)
print("Argument liczby zespolonej", cmath.phase(z))
zs=z.conjugate()
print("Sprzężenie: ", zs.conjugate())


