
import random

print("1. macierz")
size = 8
a = {}
b = {}
c = {}
for i in range(size):
    a[i] = []
    for _ in range(size):
        a[i].append(random.randint(0,10))
A=(str(a[i]))
print("Macierz A: ")
print(A)
for i in range(size):
    b[i] = []
    for _ in range(size):
       b[i].append(random.randint(0,50))
B=(str(b[i]))
print("Macierz B: ")
print(B)

for i in range(size):
    c[i] = []
    for j in range(size):
        c[i].append(a[i][j] + b[i][j])
C=(str(c[i]))
print("Pomnożone: ")
print(C)
