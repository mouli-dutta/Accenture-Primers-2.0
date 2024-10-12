def invalid_list_size():
  print('Invalid list size')

def invalid_id():
  print('Invalid Id')

def take_inp(n):
  if n <= 0:
    invalid_list_size()
    exit()

  res = []
  for _ in range(n):
    id_ = int(input())
    if id_ <= 0:
      invalid_id()
      exit()

    res.append(id_)
  return res


def non_working(l1, l2):
  return [x for x in l1 if x not in l2]


def main():
  n1 = int(input())
  first_list = take_inp(n1)

  n2 = int(input())
  second_list = take_inp(n2)

  res = non_working(first_list, second_list)
  
  print('Not working Doctors\' IDs are:')
  for r in res:
    print(r)

  return


if __name__ == '__main__':
  main()
  




























