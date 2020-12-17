import random
import time


def insert_sort(A, czas):
    for i in range(1, len(A)):
        klucz = A[i]
        j = i - 1
        while j >= 0 and A[j] > klucz:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = klucz
    print("Czas operacji: ", czas - time.process_time())
    return A


listaA = []
listaB = []
listaC = []

for i in range(0, 100, 1):
    listaA.append(random.randint(0, 20))
for i in range(0, 200, 1):
    listaB.append(random.randint(0, 20))
for i in range(0, 300, 1):
    listaC.append(random.randint(0, 20))

print(insert_sort(listaA, time.time()), '\n')
print(insert_sort(listaB, time.time()), '\n')
print(insert_sort(listaC, time.time()), '\n')


