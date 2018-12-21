mina = 2
maxa = 100
minb = 2
maxb = 100
vals = []
for a in range(mina,maxa+1):
  for b in range(minb,maxb+1):
    print("a: " + str(a) + " b: " + str(b))
    if not((a**b) in vals):
      vals.append(a**b)
vals.sort()
print(len(vals))
