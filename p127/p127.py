import functools32

@functools32.lru_cache(maxsize=10000000000)
def get_factors(x):
  factors = []
  for i in range(2, x + 1):
    while x % i == 0:
      x = x / i
      factors.append(i)
  return list(set(factors))

@functools32.lru_cache(maxsize=10000000000)
def rad(a, b, c):
  factors = []
  factors += get_factors(a)
  factors += get_factors(b)
  factors += get_factors(c)
  ret = 1
  for i in list(set(factors)):
    ret = ret * i
  return ret

@functools32.lru_cache(maxsize=10000000000)
def egcd(a, b):
  if a == 0:
    return b
  else:
    return egcd(b % a, a)

sum = 0
for c in range(3, 120000):
  if c % 100 == 0:
    print c
  for b in range(2, c):
    a = c - b
    if a < b:
      factors = []
      factors += get_factors(a)
      factors += get_factors(b)
      factors += get_factors(c)
      temp = len(factors)
      factors = list(set(factors))
      if len(factors) == temp:
        ret = 1
        for i in factors:
          ret *= i
        if ret < c:
          sum += c
print sum


