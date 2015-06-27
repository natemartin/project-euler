gap = 1
current = 1
sum = 0
while gap < 1001:
  for i in range(4):
    sum += current
    current += (gap + 1)
  gap += 2
print sum + current


