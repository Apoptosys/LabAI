'''
Created on Feb 27, 2021

@author: zahar
'''
n = int(input("n="))
items = []
for i in range(n):
    x = int(input("V[" + str(i) + "]="))
    items.append(x)

majority_elem = items[0]
count = 1
for i in range(1, len(items)):
    if items[i] == majority_elem:
        count += 1
    else: 
        count -= 1
        if count == 0:
            majority_elem = items[i]
            count = 1

print("majority element : %d" % majority_elem)
