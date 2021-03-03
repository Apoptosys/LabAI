'''
Created on Feb 27, 2021

@author: zahar
'''
from math import sqrt

x1 = int(input("X1="))
y1 = int(input("Y1="))
x2 = int(input("X2="))
y2 = int(input("Y2="))

equation = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2) 
print("Distance is:" + str(sqrt(equation)))
