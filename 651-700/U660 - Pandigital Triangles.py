chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def bc(n, b): # baseconvert(number, base)
  i = 0 # Max power of base
  while b**i < n:
    i += 1
  o = ""
  for j in range(i,-1,-1):
    x = n//(b**j)
    n -= x*(b**j)
    o += chars[x]
  if o[0] == "0":
    o = o[1:]
  return o

def is_base_pandigital(n1, n2, n3, b):
  s = bc(n1, b) + bc(n2, b) + bc(n3, b)
  return sorted(s) == sorted(chars[:b])

# Algorithm to generate integer-sided triangle with 1 angle of 120 degress
# Generate numbers for side adjacent to 120 degree angle, called s1, up to arbitrary limit
# Generate numbers for other side adjacent, called s2, up to s1
# Use cos rule to get other side, if side is integer then yay
# a^2  = b^2  + c^2  - 2bcCosA
# s3^2 = s1^2 + s2^2 - 2s1*s2*-0.5
#      = s1^2 + s2^2 + s1*s2

def is_integer(n):
  return n%1 == 0

base = 10
maxval = sum(i*base**i for i in range(base))
print(maxval)
s1 = s2 = s3 = 1
while s1 < 150:
  if not(s1%100):
    print(s1)
  for s2 in range(1, s1):
    s3 = (s1**2 + s2**2 + s1*s2)**0.5
    if is_integer(s3):
      s3 = int(s3)
      # if is_base_pandigital(s1,s2,s3,base):
      print(s1,s2,s3)
  s1 += 1
