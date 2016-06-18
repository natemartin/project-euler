cache = {}
def num_reds(spaces):
  if spaces < 0:
    return 0
  if spaces < 3:
    return 1
  if spaces == 3:
    return 2
  if spaces in cache:
    return cache[spaces]
  count = num_reds(spaces-1)
  for i in range(3, spaces+1):
    if i == spaces:
      count += 1
    count += num_reds(spaces - i - 1)
  cache[spaces] = count
  return count

print num_reds(50)
