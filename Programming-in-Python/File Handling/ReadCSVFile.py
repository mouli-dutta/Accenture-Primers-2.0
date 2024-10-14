import csv

file_path = 'OneDayInternational.csv'

with open(file_path, mode='r') as file:
    reader = csv.DictReader(file)
    for row in list(reader)[:10]:
        print(row)
