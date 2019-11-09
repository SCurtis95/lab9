import os
import csv

bName = open('2000_BoysNames.txt', 'r')
gName = open('2000_GirlsNames.txt', 'r')
dict1 = {}  ##Create dictionries to store txt files in
dict2 = {}
header = ['Name', 'Count']
for line in bName:
    (key,val) = line.split()  ##Split line into key value function for the dictionary
    dict1[key] = val        ##Pairs key and val 
bName.close()               ##Closing the text file

    
with open('2000_BoysNames.csv', 'w') as csvFile:
    input = csv.writer(csvFile, delimiter=',') 
    input.writerow(['Name', 'Count'])       ##This is my header
    for key, val in dict1.items():
        input.writerow([key,val])


for line in gName:
    (key,val) = line.split() 
    dict2[key] = val
gName.close()

with open('2000_GirlsNames.csv', 'w') as csvFile:
    fields = ['First Name', 'Count']
    input = csv.writer(csvFile, delimiter=',')
    input.writerow(['Name', 'Count'])
    for key, val in dict2.items():
        input.writerow([key,val])


##TASK 2

name = input("Which list would you like to see? 1: BoysNames 2:GirlsNames ")
if name == 1:
    with open