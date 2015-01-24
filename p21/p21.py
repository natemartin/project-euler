def divisor_sum(n):
    divs = []
    for i in range(1,n):
        if n%i == 0:
            divs.append(i)
    return sum(divs)

def is_amicable(n):
    div_sum = divisor_sum(n)
    if n == divisor_sum(div_sum) and div_sum != n:
        return True
    return False

total = 0
for i in range(1,10000):
    if is_amicable(i):
        total+=i
print total


