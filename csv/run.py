import csv

with open('teachers.csv', newline='') as csvfile:
    myreader = csv.reader(csvfile, delimiter = '|')
    rows = list(myreader)
    for row in rows[:]:
        print(', '.join(row))

# out:
# firstname,lastname,topic

# siyamak,abasnezhad,python

# diyana,mohamadi,django