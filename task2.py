import os
import csv

name = input("Which list would you like to see? 1: BoysNames 2:GirlsNames ")
if name == '1':
    with open ('2000_BoysNames.csv', 'r') as csvfile:
        read = csv.reader(csvfile, delimiter=',')
        bList = list(read)
        print(bList)
        
elif name == '2':
    with open ('2000_GirlsNames.csv', 'r') as csvfile:
        read = csv.reader(csvfile, delimiter = ',')
        gList = list(read)
        print(gList)
