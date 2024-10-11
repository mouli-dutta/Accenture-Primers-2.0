def check(row, n):
  if n % row == 1 or n % row == 0:
    print('Window Seat')
  else:
    print('Not a Window Seat')


row = int(input('Enter the number of seats per row\n'))
if row <= 0:
  print('Invalid Input')
  exit()

total = 11
t_seats = total * row

n = int(input('Enter the seat number\n'))
if n <= 0 or n > t_seats:
  print('Invalid Seat Number')
  exit()

check(row, n)
