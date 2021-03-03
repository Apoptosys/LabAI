'''
Created on Feb 27, 2021

@author: zahar
'''

current = {}

line = input()

for x in line.split(" "):
    if current.get(x, 0) == 0:
        current[x] = 1
    else:
        current[x] = current[x]+1

for x in current:
    if current[x] == 1:
        print(x+", ", end="")
