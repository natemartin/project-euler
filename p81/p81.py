f = open('matrix.txt' , 'r')
l = [map(int,line.split(',')) for line in f]

def memoize(f):
  memo = {}
  def helper(x, y):
    key = "%s-%s" % (x, y)
    if key not in memo:
      memo[key] = f(x, y)
    return memo[key]
  return helper

@memoize
def get_min_path(start_row, start_col):
  """Gets the value of the minimum path starting at the input position."""
  if start_row + 1 == len(l) and start_col + 1 == len(l[0]):
    return l[start_row][start_col]
  if start_row + 1 == len(l):
    return l[start_row][start_col] + get_min_path(start_row, start_col + 1)
  if start_col + 1 == len(l[0]):
    return l[start_row][start_col] + get_min_path(start_row + 1, start_col)
  return l[start_row][start_col] + min(get_min_path(start_row + 1, start_col), get_min_path(start_row, start_col + 1))

print get_min_path(0, 0)
