def lp(nums):
  if len(nums) == 1:
    return nums[0]
  else:
    o = []
    for num1 in sorted(nums):
      tem = nums[:]
      tem.pop(tem.index(num1))
      # print(num1,tem)
      for num2 in lp(tem):
        o.append(num1 + num2)
      if len(o) >= 1000000:
        break
    return o

print(lp(list("0123456789"))[1000000-1])