squares = []
for i in range(1,10000):
  squares.append(i**2)

maxx = 0
maxD = 0
for D in range(1,1000+1):
  if D in squares:
    continue
  # print(D)
  for s in squares:
    if (D*s + 1) in squares:
      print("%i - %i*%i = 1" %(D*s+1, D, s))
      if D*s+1 > maxx:
        maxx = D*s+1
        maxD = D
      break
print(maxD)