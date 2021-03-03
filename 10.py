'''
Created on Feb 27, 2021
Cele mai multe elemente de 1
@author: zahar
'''
def linii():
    for j in range(len(mat[0])):
        for i in range(len(mat)):
            if mat[i][j] == 1:
                return i+1

            


mat = [[0,0,0,1,1],[0,1,1,1,1],[0,0,1,1,1],[0,0,0,1,1]]


print("Linia cu cele mai multe elemente de 1 este: " + str(linii()))

    