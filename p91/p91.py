lim = 2

def is_valid_tri(x, y, i, j):
  if x == i and y == j:
    return False
  if x == 0 and y == 0:
    return False
  if i == 0 and j == 0:
    return False
  return True

def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
  return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def is_right_tri(x, y, i, j):
  len1 = ((x-i)**2 + (y-j)**2)**(1/2.0)
  len2 = ((x)**2 + (y)**2)**(1/2.0)
  len3 = ((i)**2 + (j)**2)**(1/2.0)
  if isclose(len1**2 + len2**2, len3**2):
    return True
  if isclose(len2**2 + len3**2, len1**2):
    return True
  if isclose(len3**2 + len1**2, len2**2):
    return True
  return False

count = 0
for i in range(0, lim+1):
  for j in range(0, lim+1):
    for k in range(0, lim+1):
      for l in range(0, lim+1):
        if is_valid_tri(i, j, k, l):
          if is_right_tri(i, j, k, l):
            count += 1
print count/2
