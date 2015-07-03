def is_pand_triple(a, b, c):
  s = str(a) + str(b) + str(c)
  return ''.join(sorted(s)) == '123456789'

nums = set()
for i in range(1, 999):
  for j in range(1, 9999):
    if is_pand_triple(i, j, i*j):
      nums.add(i*j)

sum = 0
for num in nums:
  sum += num
print sum
