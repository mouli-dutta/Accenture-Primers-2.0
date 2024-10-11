l, u = list(map(int, input('Enter the starting and ending numbers:\n').split()))
cnt = 0

if l < 0 or u < 0:
    print('Starting and ending numbers must be greater than or equal to zero')

elif l > u:
    print('Invalid input!! Ending number should be greater than starting number')

else:
    print(f'Armstrong numbers between {l} and {u} are:')
    
    for num in range(l, u+1):
        s = 0
        tmp = num

        while tmp > 0:
            digit = tmp % 10
            s += digit**3
            tmp //= 10

        if num == s:
            print(num)
            cnt += 1

    if cnt == 0:
        print('There is no Armstrong number between these numbers')





