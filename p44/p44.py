from sets import Set

pents = Set()
for i in range(1, 10000):
  pents.add(i * (3*i - 1) / 2)

min_d = 10000000
for i in pents:
  for j in pents:
    if abs(i - j) in pents:
      if (i + j) in pents:
        if abs(i - j) < min_d:
          min_d = abs(i - j)
print min_d
