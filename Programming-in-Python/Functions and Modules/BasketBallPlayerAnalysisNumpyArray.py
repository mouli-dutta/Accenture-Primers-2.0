import numpy as np

points = []

print('Enter John\'s points for each quarter:')

for q in range(4):
  q_points = []
  for p in range(4):
    pt = int(input(f'Quarter {q+1}, Point {p+1}: '))
    q_points.append(pt)
  points.append(q_points)


john_statistics = np.array(points)

total_first_two = john_statistics[0].sum() + john_statistics[1].sum()

avg_last_quarter = john_statistics[3].mean()


print(f'John\'s Statistics:\n{john_statistics}')
print(f'Total points scored by John in the first 2 quarters: {total_first_two:.2f}')
print(f'Average points scored by John in the last quarter: {avg_last_quarter:.2f}')



