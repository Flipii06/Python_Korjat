
import os
import random
import numpy
s=128
C = numpy.array([[1, 2, 3], [4, 5, 6]])
A=numpy.zeros((128,128), dtype=numpy.int16)
for x in range(s):
    for i in range(s):
        matrix1[x][i]=random.randint()*100
B=numpy.zeros((128,128), dtype=numpy.int16)

for x in range(s):
    for i in range(128):
        matrix2[x][i]=random.randint()*100
                          
C=numpy.zeros((128,128),dtype=numpy.int16)

for x in range(128):
    for i in range(128):
        Sum[x][i]=A[x][i]+B[x][i]
        
print (matrix1)
print (matrix2)
print(Sum)

