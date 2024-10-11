weight = float(input('Enter the weight of the person(kg):'))
height = float(input('Enter the height of the person(m):'))

if height <= 0 or weight <= 0:
  print('Provide a valid input')
  exit()

bmi = weight / (height**2)

if bmi < 18.5:
  print(f'Your BMI is {bmi:.1f} (Risk of nutritional deficiency diseases).')
  
elif 18.5 <= bmi <= 22.9:
  print(f'Your BMI is {bmi:.1f} (Low Risk).')

elif 23 <= bmi <= 27.4:
  print(f'Your BMI is {bmi:.1f} (Moderate Risk).')

else:
  print(f'Your BMI is {bmi:.1f} (High Risk).')
