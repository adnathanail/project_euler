n  = 100

wtm = {} # A 2-D dictionary where wtm[i][j] gives the number of ways to make i with combinations including j
for i in range(1,n+1): # Number trying to maker
  wtm[i] = {}
  wtm[i][i] = 1
  for j in range(1, i): # First number in addition
    s = 0
    for k in range(1, min(i-j+1, j+1)):
      s += wtm[i-j][k]
    wtm[i][j] = s

print(sum([wtm[n][x] for x in wtm[n]])-1) # -1 because sum of 2 numbers