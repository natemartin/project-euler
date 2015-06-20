import math

num_divisor_map = {}

primes = [2]
for i in range(1, 1000000):
  num = i*2 + 1
  for j in primes:
    if num % j == 0:
      break
    if j > math.sqrt(num):
      primes.append(num)
      break


def get_num_divisors(n):
  old_n = n
  total = 0
  for p in primes:
    if p > n:
      return total
    while n % p == 0:
      total += 1
      n = n/p
      if n == 1:
        if old_n == p:
          return total + 1
        return total + 2

get_num_divisors(16)


for i in range(1, 1000000):
  if get_num_divisors(i) > 5:
    print i
    break




# nth triangular number is 1 + 2 + 3 ... + n
# which is n(n + 1) / 2, or n+1 C 2
# n and n + 
