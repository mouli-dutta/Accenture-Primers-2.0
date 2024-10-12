from collections import defaultdict

n = int(input('Enter the number of courses:'))
if n < 1:
  print('Invalid no. of courses')
  exit()

sub = defaultdict(int)
for _ in range(n):
  print('Enter the name of the subject and marks respectively:')
  name = input()
  marks = int(input())

  if marks < 0 or marks > 100:
    print('Invalid mark')
    exit()

  sub[name] = marks

print('The courses you have cleared are:')
for k, v in sub.items():
  if v >= 80:
    print(f'{k} {v}')
