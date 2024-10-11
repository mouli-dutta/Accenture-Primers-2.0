def main():
  n = int(input('Enter the no. of subjects:'))

  if n <= 0:
    print('Invalid no. of subjects')
    exit()

  print('Enter the marks:')
  marks = []
  for _ in range(n):
    mark = int(input())
    if mark < 0 or mark > 100:
      print('Invalid mark')
      exit()
    marks.append(mark)

  p = 0

  for m in marks:
    if m > 50:
      p += 1
  f = len(marks) - p
  
  print(f'No. of subjects passed:{p}')
  print(f'No. of subjects failed:{f}')

  return

if __name__ == '__main__':
  main()

