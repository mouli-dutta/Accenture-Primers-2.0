def is_prime(n):
  if n < 2:
    return False

  for i in range(2, int(n**0.5)+1):
    if n % i == 0:
      return False

  return True

def find_primes(l, u):
  primes = []
  for i in range(l, u+1):
    if is_prime(i):
      primes.append(i)
  return primes



def main():
  start = int(input())
  end = int(input())

  if start < 0 or end < 0 or start > end:
    print('Invalid range')
    exit()

  primes = find_primes(start, end)

  if not primes or start == end:
    print('There are no prime numbers in this range')
    exit()

  for p in primes:
    print(p)


if __name__ == '__main__':
  main()










