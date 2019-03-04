def is_prime(n):
  for i in range(2,int(n**0.5)+1):
    if not n%i:
      return False
  return True

ps = 0
nps = 0
n = 1
d = 0
while [ps, nps] == [0,0] or ps/(ps+nps) >= 0.1: # To deal with initial division by 0 error
  d += 2
  for i in range(4):
    n += d
    if is_prime(n):
      ps += 1
    else:
      nps += 1
print(d-1)

# --- Object oriented method I really didn't want to get rid of! ---

# class Grid:
#   grid = [
#     [5, 4, 3],
#     [6, 1, 2],
#     [7, 8, 9],
#   ]
#   sl = 3 # Side length
#   def print(self):
#     [print(row) for row in self.grid]
#   def addSpiral(self):
#     self.grid.append([0 for x in range(len(self.grid[0]))]) # Bottom
#     [self.grid[i].append(0) for i in range(len(self.grid))] # Right
#     self.grid.insert(0,[0 for x in range(len(self.grid[0]))]) # Top
#     [self.grid[i].insert(0,0) for i in range(len(self.grid))] # Left
#     self.sl += 2

#     n = self.grid[-2][-2] + 1

#     for j in range(self.sl-2, -1, -1):
#       self.grid[j][-1] = n
#       n += 1
#     for i in range(self.sl-2, -1, -1):
#       self.grid[0][i] = n
#       n += 1
#     for j in range(1,self.sl):
#       self.grid[j][0] = n
#       n += 1
#     for i in range(1,self.sl):
#       self.grid[-1][i] = n
#       n += 1
#   def getDiagonals(self):
#     ds = []
#     n,m = 0, len(self.grid)-1
#     for i in range(int(len(self.grid)/2)):
#       ds.append(self.grid[n][n])
#       ds.append(self.grid[n][m])
#       ds.append(self.grid[m][n])
#       ds.append(self.grid[m][m])
#       n += 1
#       m -= 1
#     return ds

# def is_prime(n):
#   for i in range(2,int(n**0.5)+1):
#     if not n%i:
#       return False
#   return True

# def pp(l): # Percentage prime
#   return len([i for i in l if is_prime(i)])/len(l)

# g = Grid()
# g.print()

# while pp(g.getDiagonals()) >= 0.1:
#   g.addSpiral()
#   print(g.sl)