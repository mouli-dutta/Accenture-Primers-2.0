def operation(my_tuple):
  odd_sum = even_sum = 0
  for i in my_tuple:
    if i % 2 != 0:
      odd_sum += i
    else:
      even_sum += i

  return (even_sum, odd_sum)

my_tuple = (20, 5, 70, 9, 100)
sum_value = operation(my_tuple)

print('Sum of odd numbers :', sum_value[1])
print('Sum of even numbers :', sum_value[0])
