cache = {}
min_block_size = 50
def num_reds(spaces):
  if spaces < 0:
    return 0
  if spaces < min_block_size:
    return 1
  if spaces == min_block_size:
    return 2
  if spaces in cache:
    return cache[spaces]
  count = num_reds(spaces-1)
  for i in range(min_block_size, spaces+1):
    if i == spaces:
      count += 1
    count += num_reds(spaces - i - 1)
  cache[spaces] = count
  return count

for i in range(55, 1000):
  if num_reds(i) > 1000000:
    print i
    break
