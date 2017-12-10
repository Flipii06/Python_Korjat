import random

print("1. macierz")
size =3
a = {}
for i in range(size):
    a[i] = []
    for _ in range(size):
        a[i].append(random.randint(0,100))
    print(str(a[i]))

print("Wyznacznik ")
D = a[0][0] * a[1][1] * a[2][2] + a[0][1]*a[1][2]*a[2][0]+a[0][2]*a[1][0]*a[2][1]-a[0][2]*a[1][1]*a[2][0]-a[0][0]*a[1][2]*a[2][1]-a[2][2]*a[1][0]*a[0][1]
print(D)
