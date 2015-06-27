from sets import Set

def is_abundant(x):
  div_sum = 0
  for i in range(1, x):
    if x%i == 0:
      div_sum += i
  return div_sum > x

def not_abundant_sumable(abundant_nums, abundant_set, x):
  for num1 in abundant_nums:
    if x - num1 in abundant_set:
      return False
    if num1 > x:
      return True
  return True

abundant_nums = []

for i in range(28124):
  if is_abundant(i):
    print i
    abundant_nums.append(i)

abundant_set = Set(abundant_nums)

total = 0
for i in range(28124):
  if not_abundant_sumable(abundant_nums, abundant_set, i):
    print i
    total += i
print total
