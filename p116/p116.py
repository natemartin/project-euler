results = {}
results3 = {}
results4 = {}

def num_configs2(length):
  if length <=1:
    return 0
  if length <= 2:
    return 1
  if length in results.keys():
    return results[length]
  else:
    res1 = num_configs2(length-1)
    res2 = num_configs2(length-2) + 1
    results[length] = res1 + res2
  return results[length]

def num_configs3(length):
  if length <=2:
    return 0
  if length <= 3:
    return 1
  if length in results3.keys():
    return results3[length]
  else:
    res1 = num_configs3(length-1)
    res2 = num_configs3(length-3) + 1
    results3[length] = res1 + res2
  return results3[length]

def num_configs4(length):
  if length <=3:
    return 0
  if length <= 4:
    return 1
  if length in results4.keys():
    return results4[length]
  else:
    res1 = num_configs4(length-1)
    res2 = num_configs4(length-4) + 1
    results4[length] = res1 + res2
  return results4[length]

print num_configs4(50) + num_configs3(50) + num_configs2(50)
