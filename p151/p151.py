def memoize(f):
  results = {}
  def helper(x):
    key = ' '.join(str(val) for val in x)
    if key not in results:
      results[key] = f(x)
    return results[key]
  return helper

@memoize
def get_expected_value(bag):
  if bag == [5]: return 0
  total_expected = 0.0
  if len(bag) == 1: total_expected += 1
  bag.sort()
  for val in bag:
    temp = bag[:]
    temp.remove(val)
    temp.extend(range(val+1,6))
    total_expected += get_expected_value(temp)
  return total_expected / float(len(bag))
print get_expected_value([1]) - 1
