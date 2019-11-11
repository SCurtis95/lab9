import os
import csv

def generateDictionary():
    dict1={}
    
    with open('font3.txt', 'r') as letters:
        for line in letters:
            i = line.rstrip('\n')
            (key,val) = i.split(',')  
            dict1[val] = key
    letters.close()

    for key,val in dict1.items():
        code = [val]
        
        for s in val:
            s = val.lstrip('0x')
            for i in range(0,len(s),2):
                a=hex(i)
                k=int(a)
                code.append(bin(k))
            
    print(dict1)

generateDictionary()        

