import math
import matplotlib.pyplot as plt
import numpy as np
import sys

v0 = float(input("Podaj predkosc poczatkowa: "))
angle = float(input("Podaj kat rzutu w stopniach "))
angle = (angle * 3.14) / 180
g = 9.80665

v0y = v0 * math.sin(angle)
v0x = v0 * math.cos(angle)
max_height = (math.pow(v0y, 2)) / (2 * g)  # max wysokosc
Z = (math.pow(v0y, 2) * math.sin(2 * angle)) / g  # zasieg rzutu
ts = (2 * v0y) / g

print("Maksymalna wysokość na jaką wzniesie się ciało: ", max_height)
print("Zasięg rzutu: ", Z)
print("Czas od początku do upadku ", ts)

t = list(np.linspace(0, ts, 1000))
vx = [v0x for item in t]
vy = [v0y - g * item for item in t]

fig, (p1, p2, p3) = plt.subplots(3)
p1.plot(t, vx, t, vy)
p1.set(xlabel="t[s]", ylabel="v[m/s]")

vxx = [vx[0] * item for item in t]
p2.plot(t, vxx)
p2.set(xlabel="t[s]", ylabel="x[m]")

y = [item * math.tan(angle) - (g * (item * item) / (2 * vx[0] * vx[0])) for item in vxx]
p3.plot(t, y)
p3.set(ylabel="h[m]", xlabel="t[s]")
plt.show()
