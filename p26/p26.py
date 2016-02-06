from decimal import *
getcontext().prec = 1000

lim = 1000

def get_repeat_length(x):
  decx = Decimal(1) / Decimal(x)
  for i in range(1, lim):
    res = (Decimal(10**i) * decx) - decx
    if res == res.to_integral_exact():
      return i
  return 0

print get_repeat_length(7)
maxd =-1
maxi = -1
for i in range(1, 1000):
  temp = get_repeat_length(i)
  if temp > maxd:
    maxi = i
    maxd = temp
print maxi
