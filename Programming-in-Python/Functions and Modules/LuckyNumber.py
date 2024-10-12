def is_lucky(n):
  return sum(int(digit) for digit in str(n)) % 2 == 0

def main():
  n = int(input('Enter the Number:'))
  if n <= 0:
    print('Invalid Number')
    exit()

  if is_lucky(n):
    print(f'{n} is lucky')
  else:
    print(f'{n} is not lucky')

  return

if __name__ == '__main__':
  main()
