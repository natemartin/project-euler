coins = [200, 100, 50, 20, 10, 5, 2, 1]

def num_ways(total, largest):
  if total == 0:
    return 1
  ways = 0
  for i in coins:
    if i > total or i > largest:
      continue
    ways += num_ways(total - i, i)
  return ways

print num_ways(200, 200)
