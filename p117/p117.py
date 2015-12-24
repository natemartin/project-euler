
results = {}

def get_tiling(length):
  if length in results.keys():
    return results[length]
  if length == 1:
    return 1
  if length == 2:
    return 2
  if length == 3:
    return 4
  if length == 4:
    return 8
  res1 = get_tiling(length-1)
  res2 = get_tiling(length-2)
  res3 = get_tiling(length-3)
  res4 = get_tiling(length-4)
  results[length] = res1 + res2 + res3 + res4
  return results[length]

print get_tiling(50)
