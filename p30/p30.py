import math

def f(x):
  orig = x
  sum = 0
  while x > 0:
    sum += math.pow(x%10,5)
    x /= 10
  return sum == orig

sum = 0
for i in range(2, 2000000):
  if f(i):
    sum+=i
print sum
