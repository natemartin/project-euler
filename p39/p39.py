import math

counts = {}
for i in range(1, 1000):
  for j in range(1, 1000):
    result = math.sqrt(i*i + j*j)
    if result == int(result):
      circ = int(result) + i + j
      if circ <= 1000:
        if circ not in counts.keys():
          counts[circ] = 1
        else:
          counts[circ] += 1

num = 0
circ = 0
for i in counts.keys():
  if counts[i] > num:
    num = counts[i]
    circ = i
print circ
