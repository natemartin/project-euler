turns = 15

def calc(pulls, reds, fails, prob):
  if fails > turns/2:
    return 0
  if pulls == turns:
    return prob
  res1 = calc(pulls + 1, reds + 1, fails, (reds / (reds + 1.0)) * prob)
  res2 = calc(pulls + 1, reds + 1, fails + 1, (1.0 / (reds + 1)) * prob)
  return res1 + res2

# CEILING OF THIS
print 1.0 / (1 - calc(0, 1, 0, 1.0)) - 1
