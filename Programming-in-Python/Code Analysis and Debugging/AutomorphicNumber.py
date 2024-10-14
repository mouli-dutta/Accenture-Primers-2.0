def checkOdd(N):
  return N % 2 != 0

def isAutomorphic(N):
  sq = N * N
  return sq % (10**len(str(N))) == N

def main():
  print('Enter the number:')
  N = int(input())

  if checkOdd(N):
    if isAutomorphic(N):
      print('Automorphic Number')
    else:
      print('Not an Automorphic Number')
  else:
      print('Not an Odd Number')


if __name__ == '__main__':
  main()
