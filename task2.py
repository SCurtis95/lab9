import os
import csv

name = input("Which list would you like to see? 1: BoysNames 2:GirlsNames ")
if name == '1':
    with open ('2000_BoysNames.csv', 'r') as csvfile:
        bList = []      ##Creates list to store csvfile in
        i = 0       ##Counter to skip even numbered lines
        read = csv.reader(csvfile)
        for line in read:
            i+=1       ##Counter increases by 1 and then goes through if statement
            if (i % 2 != 0):  ##Modulus if statement to skip every even line 
                x=str(line).rstrip()    ##Converts to strign and strips line
                x.split(",")        ##Split list item with a ,
                bList.append(x)     ##Append string to list
    csvfile.close()
    print(bList)
    
elif name == '2':
    with open ('2000_GirlsNames.csv', 'r') as csvfile:
        gList = []
        i = 0
        read = csv.reader(csvfile)
        for line in read:
            i+=1
            if (i % 2 != 0):
                x=str(line).rstrip()
                x.split(",")
                gList.append(x)
    csvfile.close()
    print(gList)


