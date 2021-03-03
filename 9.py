'''
Created on Feb 27, 2021

@author: zahar
'''

mat = [[0, 2, 5, 4, 1], [4, 8, 2, 3, 7], [6, 3, 4, 6, 2], [7, 3, 1, 8, 3], [1, 5, 7, 9, 4]]


def suma (i1, j1, i2, j2):
    suma = 0
    for i in range (i1, i2 + 1):
        for j in range (j1, j2 + 1):
            suma = suma + mat[i][j]
    
    return suma


n = int(input("nr de perechi:"))
for i in range(n):
    line = input("Introduceti perechea de coordonate separate prin spatiu:")
    spl = line.split(" ")
    i1 = int(spl[0])
    j1 = int(spl[1])
    i2 = int(spl[2])
    j2 = int(spl[3])
    print("Suma este:" + str(suma(i1, j1, i2, j2)))
