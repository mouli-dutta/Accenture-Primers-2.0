import csv

file_path = 'OneDayInternational.csv'

with open(file_path, mode='r') as file:
    countries = {row['Versus'].strip() for row in csv.DictReader(file)}

for c in sorted(countries):
    print(c)
