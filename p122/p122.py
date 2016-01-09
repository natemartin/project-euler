powers = {}
powers[1] = 0

for i in range(6):
  newdict = {}
  for x in powers.keys():
    for y in powers.keys():
      if x+y in newdict:
        newdict[x+y] = min(newdict[x+y], powers[x] + powers[y] + 1)
      else:
        newdict[x+y] = powers[x] + powers[y] + 1
      newdict[2 * (x+y)] = newdict[x+y] + 1
  for x in newdict.keys():
    if x in powers:
      powers[x] = min(powers[x], newdict[x])
    else:
      powers[x] = newdict[x]

for i in range (1, 17):
  print "%d, %s" % (i, powers[i])
