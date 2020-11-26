f = [(2, 8), (5, 5), (9, 3), (1, 0), (3, 2), (6, 4), (1, 9), (10, 3), (2, 3), (1, 7)]
def take_second(elem):
    return elem[1]


sorted_list = sorted(f, key = take_second)
print(sorted_list)
# 2 sposób
sorted_list2 = sorted(f, key=lambda elem: elem[1])
# sorted nie nadpisuje pierwotnej listy. Jest to roznica pomiedzy sort i sorted
print(sorted_list2)