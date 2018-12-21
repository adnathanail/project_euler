def isPallindrome(n):
  return n == n[::-1]
longest_pallindrome = 0
for i in range(100,1000):
  for j in range(100,1000):
    k = i * j
    if isPallindrome(str(k)):
      longest_pallindrome = k
print(longest_pallindrome)