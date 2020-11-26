import math


def change(wej, rad):
    if rad:
        return math.degrees(wej)
    elif not rad:
        return math.radians(wej)


print(change(30, 0))
print(change(2 * math.pi, 1))
