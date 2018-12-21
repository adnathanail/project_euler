def isPallindrome(n):
  if str(int(n[::-1])) == n:
    return True
  else:
    return False
nums = []
for i in range(1,1000000):
  if isPallindrome(str(i)) and isPallindrome(bin(i)[2:]):
    print(str(i),bin(i)[2:])
    nums.append(i)
print(sum(nums))
