n = int(input('Enter the number of names:\n'))

if n <= 0:
  print('Invalid Input')
  exit()

names = []

print('Enter the names:')
for _ in range(n):
  names.append(input())

res = sorted(names, key=lambda x: (len(x), ord(x[0])), reverse=True)

print('The sorted name list is:')
for r in res:
  print(r)
