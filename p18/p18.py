triangle = []
with open('triangle.txt') as f:
  content = f.readlines()
  for line in content:
    triangle.append(map(int, line.strip().split(' ')))

# Doing the brute force recursion instead of DP because why not
def get_max_path_value(x, y):
  if x + 1 >= len(triangle):
    return triangle[x][y]
  return triangle[x][y] + max(get_max_path_value(x+1, y), get_max_path_value(x+1, y+1))
print get_max_path_value(0,0)
