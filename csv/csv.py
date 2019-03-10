import csv
exel = [['jessica', 1981]]
file = open('file.csv', 'w',newline= '')
csv.writer(file).writerows(exel)
ID = 'linux.py'