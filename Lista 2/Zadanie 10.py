list = [*range(0,100,3)]
print(list)
del(list[5:len(list):3])
print(list)
avg = (sum(list)/len(list))
print("Srednia", avg)
