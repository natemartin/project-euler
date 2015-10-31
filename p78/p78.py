
def memoize(f):
    """ Memoization decorator for functions taking one or more arguments. """
    class memodict(dict):
        def __init__(self, f):
            self.f = f
        def __call__(self, *args):
            return self[args]
        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return memodict(f)

@memoize
def num_splits(n, s):
  if s == 1:
    return 1
  if n < s:
    return num_splits(n, n)
  if n == s:
    return num_splits(n, s-1) + 1
  return num_splits(n-s, s) + num_splits(n, s-1)

for i in range(3, 10000):
  for j in range(1, i):
    num_splits(i, j)
  if num_splits(i, i) % 1000000 == 0:
    print i
    break

# xxxx
# xxx x
# xx xx
# xx x x
# x x x x

