tri_nums = []
prv = 0
for i in range(1, 1000):
  tri_nums.append(i + prv)
  prv += i


def is_tri_word(word):
  total = 0
  for c in word:
    total += (ord(c) - 64)
  if total in tri_nums:
    return True
  return False


f = open('words.txt', 'r')
words = f.read().replace('"', '').split(',')
count = 0
for word in words:
  if is_tri_word(word):
    count += 1
print count
