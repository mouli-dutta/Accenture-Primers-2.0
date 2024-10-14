def operation(mylist):
  sm = 0
  mx = mylist[0][0]
  
  for i in mylist:
    for j in i:
      if j > mx:
        mx = j
      sm += j

  return mx, sm

my_list = [[3, 5, 6], [7, 8, 44], [33, 1, 99]]
value1, value2 = operation(my_list)
print(f'{value1} is the Maximum value.')
print(f'{value2} is the Sum')
