def is_funny(s):
  r = s[::-1]

  for i in range(1, len(s)):
    if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(r[i]) - ord(r[i-1])):
      return False
  return True


def funny_string(s):
  return 'Funny' if is_funny(s) else 'Not Funny'



def main():
  inp = input('Enter the string:')
  n = len(inp)

  if 2 <= n <= 50:
    print(funny_string(inp))
  else:
    print('Invalid string')


if __name__ == '__main__':
  main()








