def is_weird_fraction(a, b):
  #Check each digit in the numerator
  a_nums = list(str(a))
  b_nums = list(str(b))
  if a_nums.count('0') > 0 or b_nums.count('0') > 0:
    return False
  if a_nums[0] in b_nums:
    temp = b_nums[:]
    temp.remove(a_nums[0])
    if a / float(b) == float(a_nums[1]) / float(temp[0]):
      return True
  if a_nums[1] in b_nums:
    temp = b_nums[:]
    temp.remove(a_nums[1])
    if a / float(b) == float(a_nums[0]) / float(temp[0]):
      return True
  return False

num = 1
denom = 1
for i in range(10, 100):
  for j in range(i+1, 100):
    if is_weird_fraction(i,j):
      num *= i
      denom *= j
      print str(i) + " " + str(j)
print str(num) + "/" + str(denom)
