import random
a=[]
for x in range(50):
 a.append(random.randint(1,200))
print('Nieposortowane:', a)
for i in range(50):
        for j in range(49):
            if a[j] > a[j+1]:
                tmp = a[j]                
                a[j] = a[j+1]
                a[j+1] = tmp
print('Posortowane:', a)
