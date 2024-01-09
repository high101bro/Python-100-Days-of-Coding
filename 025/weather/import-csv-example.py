#! /usr/bin/env python3

# with open('weather.csv', 'r') as file:
#     data = file.readlines()
#
# print(data)

import csv

with open("weather.csv", 'r') as file:
    csv = csv.reader(file)
    temperatures = []
    for row in csv:
        if row[1] == 'temp':
            pass
        else:
            temperatures.append(int(row[1]))
        # print(row)
    print(temperatures)
