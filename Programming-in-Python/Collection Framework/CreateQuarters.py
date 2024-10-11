months = ['January', 'February', 'March', 
           'April',   'May',     'June',
           'July',    'August',  'September',
           'October', 'November', 'December']

print('Months in expanded form:')
for m in months:
  print(m)

print('\nThe four quarters are:\n')

print('First Quarter:')
for m in months[:3]:
  print(m)


print('\nSecond Quarter:')
for m in months[3:6]:
  print(m)


print('\nThird Quarter:')
for m in months[6:9]:
  print(m)


print('\nFourth Quarter:')
for m in months[9:]:
  print(m)





