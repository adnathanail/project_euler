# Run this to see why the numbers can't go above 6 figures
# for k in range(1,10):
#   n = (k+1)*(9**5)
#   print("largest %i digit sum is %i which is %i digits" % (k+1, n, len(str(n))))

i = 10
ns = []
while i < 999999:
  t = 0
  for j in str(i):
    t += int(j)**5
  if i == t:
    ns.append(i)
    # print(i, t)
  i += 1
print(sum(ns), ns)