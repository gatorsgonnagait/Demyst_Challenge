# -*- coding: utf-8 -*-
"""
Created on Sun May 31 19:19:16 2020
"""
import json
import csv

f = open('spec.json')
data = json.load(f)
f.close()
list1 = data['ColumnNames']
list2 = data['Offsets']
columns = tuple(map(tuple, zip(list1, list(map(int, list2)))))
with open('myfile.txt', 'w', encoding='cp1252') as f:
    f.write(''.join([(field_name).ljust(width) for field_name, width in columns]))


def cuts(x, l):
    location = 0
    for length in l:
        yield x[location:location + length]
        location += length


with open("myfile.txt") as f:
    for line in f:
        with open('mycsv.csv', 'w', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(list(cuts(line, list(map(int, list2)))))