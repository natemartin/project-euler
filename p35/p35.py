def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]
prime_set = set()
for i in primes(10000000):
  prime_set.add(i)

def is_circular(n):
  if len(str(n)) == 1:
    return True
  current = str(n)
  for i in range(len(str(n))):
    c = current[0]
    current = current[1:] + current[0]
    if int(current) not in prime_set:
      return False
  return True

count = 0
for i in prime_set:
  if is_circular(i):
    count += 1
print count
