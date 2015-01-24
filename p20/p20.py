def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

total = 0
nums = list(str(factorial(100)))

for n in nums:
    total+=int(n)
print total




