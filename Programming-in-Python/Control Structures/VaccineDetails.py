while True:
  try:
    people = int(input('Enter the total no of people in the area:'))
    if people <= 0:
      print('Invalid Input')
      break

    s_dose = int(input('Single-dose count:'))
    if s_dose < 0 or s_dose > people:
      print('Invalid Input')
      break

    d_dose = int(input('Double-dose count:'))
    if d_dose < 0 or d_dose > people:
      print('Invalid Input')
      break

    if s_dose + d_dose > people:
      print('Invalid Input')
      break


    non_vaccinated = people - (s_dose + d_dose)
    percentage = (d_dose / people) * 100

    print('Not vaccinated people count:', non_vaccinated)
    print(f'Total vaccinated percentage of people:{percentage:.2f}')

    nxt = int(input('Do you want to continue (1) for yes (0) for no:'))

    if nxt == 1:
      continue
    elif nxt == 0:
      break
    else:
      print('Invalid Input')
      break

  except ValueError:
    print('Invalid Input')
      break


