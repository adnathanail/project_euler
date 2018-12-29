def generate_val(a, b, n):
  return n**2 + a*n + b

def isprime(n):
  if n in [1,2]:
    return n == 2
  if n < 1:
    return False
  for i in range(3,int(n/2)+1,2):
    if n%i == 0:
      return False
  return True

maxi = maxa = maxb = 0
for a in range(-999, 1000):
  for b in range(-999, 1000):
    i = 0
    while isprime(generate_val(a,b,i)):
      i += 1
    # print(a, b, i)
    if i > maxi:
      maxi = i
      maxa = a
      maxb = b
#   print(a)
# print(maxi, maxa, maxb)
print(maxa*maxb)