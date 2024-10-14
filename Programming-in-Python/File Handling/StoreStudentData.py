no = int(input('Enter number of students:'))

with open('output_data.txt', 'w') as file:
    for i in range(1, no + 1):
        print(f'Student {i}')
        name = input('Enter name:')
        score = input('Enter the score:')
        file.write(f'Name: {name} Score: {score}\n')

with open('output_data.txt', 'r') as file:
    print(file.read())
