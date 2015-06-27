def is_integer(n):
  return int(n) == n
def get_repeat_period(n):
  orig = 1.0 / n
  shifted = orig * 10
  length = 1
  while(not is_integer(shifted - orig)):
    length += 1
    shifted *= 10
  return length



print get_repeat_period(7)
