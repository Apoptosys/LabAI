'''
Created on Feb 27, 2021

@author: zahar
'''

line = input("Insert text:")
maxWord = line[0]
ok = True
for x in range(1,len(line)):
    if line[x] == " ":
        ok = False
        continue
    
    
    if line[x-1] == " ":
        if line[x] > maxWord[0]:
            maxWord = ""
            ok = True
            
    if ok == True:
        maxWord = maxWord + line[x]
    
    
print(maxWord)
