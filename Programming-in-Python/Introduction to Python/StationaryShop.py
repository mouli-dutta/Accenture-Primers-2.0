def format(val):
  return f'{val:.2f}'

c1 = float(input('Cost of A4sheet:\n'))
if c1 < 0:
  print('Invalid input')
  exit()

c2 = float(input('Cost of pen:\n'))
if c2 < 0:
  print('Invalid input')
  exit()

c3 = float(input('Cost of pencil:\n'))
if c3 < 0:
  print('Invalid input')
  exit()

c4 = float(input('Cost of eraser:\n'))
if c4 < 0:
  print('Invalid input')
  exit()


print('Items Details')
print('A4sheet:' + format(c1))
print('Pen:' + format(c2))
print('Pencil:' + format(c3))
print('Eraser:' + format(c4))

