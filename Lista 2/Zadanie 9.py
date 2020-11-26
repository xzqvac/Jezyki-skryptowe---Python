import itertools
c = list(itertools.chain([2, 4, 3], [1, 5, 6], [9], [7, 9, 0]))
# bierze wszystkie listy i kazdy element z nich(poniewaz listy sa interowalne) i zwraca całość jako pojedyczna liste
print(type(c))
print(c)