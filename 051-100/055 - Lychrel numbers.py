def is_palindromic(n):
  s = str(n)
  return s == s[::-1]

def is_lychrel(n):
  i = 0
  while not is_palindromic(n) or i == 0: # or i == 0 to deal with palindromic lychrels
    n = n + int(str(n)[::-1])
    i += 1
    if i >= 50:
      return True
  return False

print(len([i for i in range(10,10000) if is_lychrel(i)]))