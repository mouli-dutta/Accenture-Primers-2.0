def invalid():
  print('Invalid')

def valid_age(age):
  return 21 <= age <= 58

def valid_band(band):
  return band in ['A', 'B', 'C', 'D']

def take_inp():
  name = input('Name:')

  age = int(input('Age:'))
  if not valid_age(age):
    invalid()
    exit()

  designation = input('Designation:')

  band = int(input('Band:'))
  if not valid_band(band):
    invalid()
    exit()

  return (name, age, designation, band)


def interests(interest, list_of_residents):
  return [i for i in list_of_residents if interest in i]


def main():
  list_of_residents = []
  n = int(input('No of Residents:'))
  if n <= 0:
    invalid()
    exit()

  for i in range(n):
    print(f'Resident {i+1}:')
    list_of_residents.append(take_inp())

  print(('NAME', 'AGE', 'DESIGNATION', 'BAND'))
  for l in list_of_residents:
    print(l)

  interest = input('Enter your band of interest:')
  if not valid_band(interest):
    invalid()
    exit()

  print(('NAME', 'AGE', 'DESIGNATION', 'BAND'))
  bands = interests(interest, list_of_residents)
  if bands:
    for b in bands:
      print(b)

  else: print('No resident under this band')



if __name__ == '__main__':
  main()















