import greet

name = input()
print(greet.message, end=', ')
greet.greet(name)
print('Documentation string:', greet.greet.__doc__)
