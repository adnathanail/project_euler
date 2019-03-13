def is_anagram(a,b):
  return sorted(str(a)) == sorted(str(b))

def are_anagrams(l):
  n = l[0]
  for i in range(1,len(l)):
    if not is_anagram(n, l[i]):
      return False
  return True

found = False
i = 1
while not found:
  if are_anagrams([i, 2*i, 3*i, 4*i, 5*i, 6*i]):
    found = True
  else:
    i += 1
print(i)