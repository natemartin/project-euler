# ATTEMPT #1 (too slow)
sq = []
count = 0
for i in range(4):
  sq.append([-1,-1,-1,-1])

def is_partially_valid(row, col, target_sum):
  # Validate the completed rows, cols, and diags of the square.

  # Rows
  if col == 3:
    sum = 0
    incomplete = False
    for j in range(4):
      if sq[row][j] == -1:
        incomplete = True
        break
      sum += sq[row][j]
    if not incomplete and sum != target_sum:
      return False

  # Cols
  if row == 3:
    sum = 0
    incomplete = False
    for j in range(4):
      if sq[j][col] == -1:
        incomplete = True
        break
      sum += sq[j][col]
    if not incomplete and sum != target_sum:
      return False

  # Diag1
  if row == col:
    sum = 0
    incomplete = False
    for i in range(4):
      if sq[i][i] == -1:
        incomplete = True
        break
      sum += sq[i][i]
    if not incomplete and sum != target_sum:
      return False

  # Diag2
  if 3 - row == col:
    sum = 0
    incomplete = False
    for i in range(4):
      if sq[3-i][i] == -1:
        incomplete = True
        break
      sum += sq[3-i][i]
    if not incomplete and sum != target_sum:
      return False

  return True

def get_next_cords(i, j):
  if i < 3:
    i +=1
  else:
    i = 1
    j += 1
  return i, j

def fill_square(i, j, target_sum):
  # print "Filling " + str(i) + " " + str(j)
  if j > 3:
    global count
    count += 1
    return
  for val in range(10):
    sq[i][j] = val
    if is_partially_valid(i, j, target_sum):
      next_i, next_j = get_next_cords(i, j)
      fill_square(next_i, next_j, target_sum)
    sq[i][j] = -1

for i in range(10):
  sq[0][0] = i
  for j in range(10):
    sq[0][1] = j
    print j
    for k in range(10):
      sq[0][2] = k
      for l in range(10):
        sum = i+j+k+l
        sq[0][3] = l
        fill_square(1, 0, sum)
print count


