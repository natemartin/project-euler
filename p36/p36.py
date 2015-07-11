def is_palindrome(n):
  str_n = str(n)
  for i in range(len(str_n) / 2):
    if str_n[i] != str_n[len(str_n) - 1 - i]:
      return False
  return True

sum = 0
for i in range(1000000):
  if is_palindrome(i) and is_palindrome(int(bin(i)[2:])):
    sum += i
print sum
