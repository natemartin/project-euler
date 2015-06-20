ones_place = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4}
teens = {10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8}
tens = {2:6, 3:6, 4:5, 5:5, 6:5, 7:7, 8:6, 9:6}

total = 0

def get_chars(n):
    if n == 0:
        return 0
    if n < 10:
        return ones_place[n]
    if n < 20:
        return teens[n]
    if n < 100:
        tens_place = n/10
        resid = n%10
        return tens[tens_place] + ones_place[resid]
    if n < 1000:
        hundreds = n/100
        resid = n % 100
        if resid > 0:
            return ones_place[hundreds] + 10 + get_chars(resid)
        return ones_place[hundreds] + 7
    return 11

total = 0
for i in range(1, 1001):
    print str(i) + " - " + str(get_chars(i))
    total+=get_chars(i)
print total


