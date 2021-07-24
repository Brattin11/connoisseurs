import csv
import math

WEIGHTS = [0.2, 0.2, 0.17, 0.14, 0.11, 0.09, 0.06, 0.03]

datafile = open("MexicanConnoisseurs.csv", "r")
datareader = csv.reader(datafile, delimiter=",")
next(datareader)  # skip the first line (column headers)
data = []
locations = []


for row in datareader:
    data.append(row[1:])
    locations.append(row[0])

averages = []

for row in data:
    average = 0
    i = 0
    location = 0
    for number in row:
        average = average + (int(number) * WEIGHTS[i])
        i += 1

    print(locations[location] + ":", round(average, 2))
    location += 1
