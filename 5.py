'''
Created on Feb 27, 2021

@author: zahar
'''

n = int(input("n="))
suma = 0
for i in range(n):
    x = int(input("V[" + str(i) + "]="))
    suma = suma + x

print(suma - n * (n - 1) / 2)
