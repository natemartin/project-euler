nums = [0,1,2,3,4,5,6,7,8,9]

def get_perms(sorted_nums):
  if len(sorted_nums) == 1:
    return [sorted_nums]
  perms = []
  for i in sorted_nums:
    temp = sorted_nums[:]
    temp.remove(i)
    sub_perms = get_perms(temp)
    for j in sub_perms:
      perms.append([i] + j)
  return perms

print get_perms(nums)[999999]
