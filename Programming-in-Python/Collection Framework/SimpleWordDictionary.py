def main():
    dictionary = {}

    while True:
        word = input('Enter the word:')
        try:
            n = int(input('Enter the no of meanings:'))
            if n <= 0:
                print('Invalid Input')
                if dictionary:
                    print('\nHere\'s the dictionary you\'ve created:')
                    for k, v in dictionary.items():
                        print(f'{k}:{v}')
                exit()
            meanings = []
            print('Enter the meanings:')
            for i in range(n):
                meanings.append(input())
            dictionary[word] = meanings

            choice = input('Do you want to add one more elements to the dictionary? If yes, press 1, else press 0:')
            if choice == '0':
                break
            elif choice != '1':
                print('Invalid Input')
                break

        except ValueError:
            print('Invalid Input: Please enter a valid number for the number of meanings.')
            break

    print('\nHere\'s the dictionary you\'ve created:')
    for k, v in dictionary.items():
        print(f'{k}:{v}')

    return

if __name__ == '__main__':
    main()








