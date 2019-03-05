def is_inc(n):
  s = str(n)
  for i in range(len(s)-1):
    if int(s[i+1]) < int(s[i]):
      return False
  return True
def is_dec(n):
  s = str(n)
  for i in range(len(s)-1):
    if int(s[i+1]) > int(s[i]):
      return False
  return True
is_bouncy = lambda n: not (is_inc(n) or is_dec(n))

bs = 0
nbs = 0
i = 0
while bs == 0 or bs/(bs+nbs) != 0.99: # bs == 0 to handle division by zero at start
  i += 1
  if is_bouncy(i):
    bs += 1
  else:
    nbs += 1
print(i)