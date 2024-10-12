import numpy as np

pixels = []

print('Enter pixel values for the image (8 values):')
for i in range(8):
  val = int(input(f'Pixel {i+1}:'))
  if 0 <= val <= 256:
    pixels.append(val)
  else:
    print('Invalid input! Enter a value between 0 and 256')


print('Original Array:')
print(np.array(pixels))

image_matrix = np.array(pixels).reshape(2, 4)
print('Image Matrix (2x4):')
print(image_matrix)

top_left = image_matrix[0:1, 0:2]
print('Top-left 2x2 Region:')
print(top_left)

bottom_right = image_matrix[1:2, 2:4]
print('Bottom-right 2x2 Region:')
print(bottom_right)

mean = image_matrix.mean()
print(f'Mean value of the pixel values in the Image Matrix: {mean:.2f}')









