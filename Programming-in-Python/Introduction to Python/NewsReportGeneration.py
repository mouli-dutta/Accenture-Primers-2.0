dead_cnt = int(input('Dead Count:\n'))

if dead_cnt < 0:
  print('Invalid input')
  exit()

inj_cnt = int(input('Injured Count:\n'))
if inj_cnt < 0:
  print('Invalid input')
  exit()

safe_cnt = int(input('Safe Count:\n'))
if safe_cnt < 0:
  print('Invalid input')
  exit()

print('TSUNAMI REPORT OF JAPAN')
print('The number of people')
print(f'Dead: {dead_cnt}')
print(f'Injured: {inj_cnt}')
print(f'Safe: {safe_cnt}')
print('Please help the people who are suffering!!!')




