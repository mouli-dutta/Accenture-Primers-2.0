n = int(input('Enter a number:'))

if n < 0:
  print('Factorial does not exist for negative numbers')
else:
  f = 1
  for i in range(1, n+1):
    f *= i

  print('Factorial is', f)
