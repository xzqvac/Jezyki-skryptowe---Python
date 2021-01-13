import math
import matplotlib.pyplot as plt
import numpy as np
import sys


v0 = float(input("Podaj predkosc poczatkowa: "))
angle = float(input("Podaj kat rzutu: "))
angle = (angle * 180) / math.pi
g = 9.80665
v0y = v0 * math.sin(angle)
v0x = v0 * math.cos(angle)
max_height = math.pow(v0y, 2) / 2*g
Z = (math.pow(v0y, 2) * math.sin(2*angle))/g
ts = 2*v0y/g

print("Maksymalna wysokość na jaką wzniesie się ciało: ", max_height)
print("Zasięg rzutu: ", Z)
print("Czas od początku do upadku ", ts)

t = np.linspace(0, ts, 10)
x = v0x * t
plt.subplot(1, 3, 1)
plt.plot(t, x)  # wykres polozenia w funkcji czasu
plt.show()


plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
