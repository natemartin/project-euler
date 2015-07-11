def fact(n):
  if n < 2:
    return 1
  return n * fact(n - 1)
def fact_sum(n):
  sum = 0
  for c in str(n):
    sum += fact(int(c))
  return sum == n

sum = 0
for i in range(3, 1000000):
  if fact_sum(i):
    sum += i

print sum

