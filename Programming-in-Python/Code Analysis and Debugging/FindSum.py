def main():
  print('Enter the value of N')
  number = int(input())
  sm = 0
  if number < 0:
    print('Invalid input')
  else:
    for i in range(1, number+1):
      sm = sm + i
    print(f'The sum of first {number} natural numbers is {sm}')

if __name__ == '__main__':
  main()
