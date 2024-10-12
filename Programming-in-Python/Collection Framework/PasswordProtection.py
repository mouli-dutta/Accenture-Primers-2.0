n = int(input('Enter the total no. of plots:'))
if n < 1 or n > 20:
  print('Invalid Input')
  exit()

plot = []
print('Enter the number of each plot:')
for _ in range(n):
  p = int(input())
  if p <= 0:
    print('Invalid Input')
    exit()
  plot.append(p)

avg = sum(plot) / 2
print(f'The password for the file is:{avg:.2f}')
