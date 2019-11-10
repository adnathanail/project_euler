def ways_to_make(n):
  wtm = {} # A 2-D dictionary where wtm[i][j] gives the number of ways to make i with combinations where the highest number is j
  for i in range(1,n+1):
    wtm[i] = {i: 1} # There is 1 way to make i with i
    for j in range(1, i):
      s = 0 # Ways to make i using j
      for k in range(1, min(i-j, j)+1): # j<i/2 gap between i and j is made of 1's  |  j>i/2 gap between i and j is j
        s += wtm[i-j][k]
      wtm[i][j] = s
  return sum([wtm[n][x] for x in wtm[n]]) - 1 # -1 because 100 on its own is not a valid solution ("sum of at least TWO positive integers")

print(ways_to_make(100))