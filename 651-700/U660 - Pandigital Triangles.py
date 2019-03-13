chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def bc(n, b): # baseconvert(number, base)
  i = 0 # Max power of base
  while b**i < n:
    i += 1
  # print(i)
  o = ""
  for j in range(i,-1,-1):
    x = n//(b**j)
    n -= x*(b**j)
    o += chars[x]
    # print(j, x, n, o)
  if o[0] == "0":
    o = o[1:]
  return o

def is_base_pandigital(n1, n2, n3, b):
  s = bc(n1, b) + bc(n2, b) + bc(n3, b)
  return sorted(s) == sorted(chars[:b])

# Algorithm to generate integer-sided triangle with 1 angle of 120 degress
# Side opposite 120 degrees must be bigger than other 2
# Generate numbers for this side starting from 3, called s1
# Generate numbers for either of the other sides up to s1, called s2
# Generate numbers for third side up to s2, called s3
# This way no duplicate triplets will be generated
# Use cos rule to check if each triplet gives an angle of 120
# cosA = (b^2 + c^2 - a^2)/2bc
# cos(120) = -0.5

def cosA(a, b, c):
  return (b**2 + c**2 - a**2)/(2 * b * c)

base = 10
maxval = sum([i*base**i for i in range(base)])
print(maxval)
s1 = s2 = s3 = 1
while s1 + s2 + s3 < maxval:
  print(s1)
  for s2 in range(1, s1):
    s3 = 1
    while cosA(s1, s2, s3) < -0.5 and s3 < s2:
      s3 += 1
    if cosA(s1, s2, s3) == -0.5 and is_base_pandigital(s1, s2, s3, base):
      print(base, s1, s2, s3)
  s1 += 1

print(cosA(403, 248, 217))