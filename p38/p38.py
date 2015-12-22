def is_pand(x):
  return ''.join(sorted(list(x))) == "123456789"

def get_pand_max(x):
  current = str(x)
  mult = 2

  while len(current) < 9:
    current += str(mult * x)
    mult += 1
  if is_pand(current):
    return int(current)
  return 0

max_pand = 0
for i in range(1, 1000000):
  current = get_pand_max(i)
  if current > max_pand:
    max_pand = current
print max_pand
