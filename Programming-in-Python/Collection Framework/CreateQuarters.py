months = ['January', 'February', 'March', 'April', 'May', 'June', 
           'July', 'August', 'September', 'October', 'November', 'December']

print('Months in expanded form:')
print('\n'.join(months))

quarters = ['First', 'Second', 'Third', 'Fourth']
for i, quarter in enumerate(quarters):
    print(f'\n{quarter} Quarter:')
    print('\n'.join(months[i * 3: (i + 1) * 3]))
