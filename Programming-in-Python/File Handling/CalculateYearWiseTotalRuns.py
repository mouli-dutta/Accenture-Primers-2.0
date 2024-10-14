import csv
from collections import defaultdict

file_path = 'OneDayInternational.csv'

year_wise_run = defaultdict(int)

with open(file_path, mode='r') as file:
    for row in csv.DictReader(file):
      match_date = row['MatchDate'].strip()
      runs = int(row['Runs'].strip())
      
      year = match_date.split('/')[-1]
      
      year_wise_run[year] += runs

for year, total_runs in sorted(year_wise_run.items()):
    print(f'{year} {total_runs}')
