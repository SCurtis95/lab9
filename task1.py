import os
import csv

bName = open('2000_BoysNames.txt', 'r')
gName = open('2000_GirlsNames.txt', 'r')
dict1 = {}
dict2 = {}
header = ['Name', 'Count']
for line in bName:
    (key,val) = line.split()  ##Split line into key value function for the dictionary
    dict1[key] = val
bName.close()

    
with open('2000_BoysNames.csv', 'w') as csvFile:
    fields = ['First Name', 'Count']
    input = csv.writer(csvFile, delimiter=',')
    input.writerow(['Name', 'Count'])
    for key, val in dict1.items():
        input.writerow([key,val])

for line in gName:
    (key,val) = line.split()  ##Split line into key value function for the dictionary
    dict2[key] = val
gName.close()

with open('2000_GirlsNames.csv', 'w') as csvFile:
    fields = ['First Name', 'Count']
    input = csv.writer(csvFile, delimiter=',')
    input.writerow(['Name', 'Count'])
    for key, val in dict2.items():
        input.writerow([key,val])