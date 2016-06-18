nums = [0,1,2,3,4,5,6,7,8,9]
choices = set()

def build_sets(possible, current):
  if len(current) > 5:
    choices.add(frozenset(current))
    return
  if len(possible) < 1:
    return
  temp = set(current)
  temp2 = list(possible)
  temp.add(temp2.pop())
  build_sets(temp2, temp)
  build_sets(temp2, current)

build_sets(nums, set())

def has_all_squares(s1, s2):
  s1 = set(s1)
  s2 = set(s2)
  possib = set()
  if 6 in s1:
    s1.add(9)
  if 6 in s2:
    s2.add(9)
  if 9 in s1:
    s1.add(6)
  if 9 in s2:
    s2.add(6)
  for i in s1:
    for j in s2:
      possib.add(int(str(i) + str(j)))
      possib.add(int(str(j) + str(i)))
  for i in range(1, 10):
    if i*i not in possib:
      return False
  return True

count = 0
for d1 in choices:
  for d2 in choices:
    if has_all_squares(d1, d2):
      count += 1
print count/2
