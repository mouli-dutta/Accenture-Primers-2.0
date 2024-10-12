def fibonacci(n):
  if n <= 1:
    return n

  a, b = 0, 1
  for _ in range(2, n+1):
    a, b = b, a+b

  return b


def main():
  month = int(input('Enter the month as numeric value:'))

  if month < 1 or month > 12:
    print('Invalid month')
    exit()

  print(f'The amoeba size is {fibonacci(month-1)}')


if __name__ == '__main__':
  main()











