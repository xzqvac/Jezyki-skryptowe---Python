from itertools import combinations, chain


class sublists:
    def __init__(self, lista):
        self.lista = lista
        self.sublists = []

    def return_sublists(self):
        for i in range(len(self.lista) + 1):
            sublist = list(combinations(self.lista, i))
            self.sublists.append(sublist)
        self.sublists = list(chain(*self.sublists))
        for i in self.sublists: print(i)
        return self.sublists


p1 = sublists([1, 2, 3, 4])
p1.return_sublists()
