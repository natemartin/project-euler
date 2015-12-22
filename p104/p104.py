def is_pand(x):
  return ''.join(sorted(list(x))) == "123456789"

i = 1
j = 1

for ind in range(1, 200000):
  temp = i + j
  i = j
  j = temp
  if is_pand(str(i)[:9]) and is_pand(str(i)[-9:]):
    print ind+1
  
