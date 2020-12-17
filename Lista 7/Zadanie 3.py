import random
import time


def bubble_sort(data, czas):
    for i in range(len(data) - 1, 0, -1):
        for j in range(i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    print("Czas operacji: ", czas - time.process_time())
    return data


listaA = []
listaB = []
listaC = []

for i in range(0, 100, 1):
    listaA.append(random.randint(0, 20))
for i in range(0, 200, 1):
    listaB.append(random.randint(0, 20))
for i in range(0, 300, 1):
    listaC.append(random.randint(0, 20))

print(bubble_sort(listaA, time.time()), '\n')
print(bubble_sort(listaB, time.time()), '\n')
print(bubble_sort(listaC, time.time()), '\n')



