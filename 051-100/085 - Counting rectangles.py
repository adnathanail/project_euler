# In a 5x4 rectangle
# For a sub-rectangle of width 1 there can be 5, width 2:4, 3:3, 4:2, 5:1
# Vertically, sub-rectangle of height 1 there can be 4, 2:3, 3:2, 4:1
# Therefore for rectangles of, say, width 4 and height 2 there can be 2*3 = 6 rectangles
# The total number of rectangles in the 5x4 is:
#   (1*1 + 1*2 + 1*3 + 1*4) + (2*1 + 2*2 + 2*3 + 2*4) + (3*1 + 3*2 + 3*3 + 3*4) + (4*1 + 4*2 + 4*3 + 4*4) + (5*1 + 5*2 + 5*3 + 5*4)
# = 1(1+2+3+4) + 2(1+2+3+4) + 3(1+2+3+4) + 4(1+2+3+4) + 5(1+2+3+4)
# = (1+2+3+4+5)(1+2+3+4)
# = (Σ1->5)(Σ1->4)
# Σ1->n = 0.5*n*(n+1)
def sut(n):
  return int(0.5*n*(n+1))

def recs(a, b):
  return sut(a)*sut(b)

# recs(2000, 1) = 2001000 > 2000000
# Therefore max i is 2000

coms = []
for i in range(1,2000):
  j = 2
  while recs(i,j) < 2000000:
    j += 1
  coms.append([i*j, abs(2000000 - recs(i, j))])
  coms.append([i*(j-1), abs(2000000 - recs(i, j-1))])

print(sorted(coms, key=lambda x: x[1])[0][0])