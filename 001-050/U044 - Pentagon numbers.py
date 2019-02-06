gen_pens = lambda n: [int(0.5*i*(3*i-1)) for i in range(1,n)]
lp = 5000
pens = gen_pens(lp)

for i in range(lp):
  for j in range(i,lp):
    if (pens[i]+pens[j]) in pens and (pens[i]-pens[j]) in pens:
      print(pens[i], pens[j])