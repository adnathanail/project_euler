# For a given number i
# To be multipled by 1..n
# When i is a minimum (1)
# n would have to be 9 so n < 10
# "9999" + "19998" has 9 digits
# "10000" + "20000" has 10 digits
# So i < 10000
def pandigital(n):
  return sorted(str(n)) == sorted('123456789')

pands = []
for i in range(9999+1):
  conc = ""
  for n in range(1,9+1):
    conc += str(i * n)
    if pandigital(conc):
      pands.append(int(conc))
      print(i,n,conc)
    if int(conc) > 987654321:
      break
print(max(pands))