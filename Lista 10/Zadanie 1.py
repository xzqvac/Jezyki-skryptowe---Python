import cmath


class kolo:
    def __init__(self, r):
        self.r = r

    def pole(self):
        return (self.r ** 2) * cmath.pi

    def obwod(self):
        return 2 * self.r * cmath.pi


p1 = kolo(10)
print(p1.pole(), p1.obwod())
