input = open('p107_network.txt')
row = 0
edges = []
total = 0
for i in input:
  col = 0
  for j in i.strip().split(','):
    if j != '-':
      edges.append((row, col, int(j)))
      total += int(j)
    col += 1
  row += 1

def compare_edges(e1, e2):
  return e1[2] - e2[2]
edges.sort(cmp=compare_edges)

sets = []
for i in range(row):
  sets.append(i)

def find(x):
  if sets[x] == x:
    return x
  else:
    return find(sets[x])

def union(x, y):
  xroot = find(x)
  yroot = find(y)
  if xroot == yroot:
    return
  sets[yroot] = xroot

sum = 0
for e in edges:
  if find(e[0]) != find(e[1]):
    union(e[0], e[1])
    sum += e[2]

print total/2 - sum

