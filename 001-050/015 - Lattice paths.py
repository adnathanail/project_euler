gridSize = 20
grid = []
for i in range(gridSize+1):
  grid.append([])
  for j in range(gridSize+1):
    grid[-1].append(0)
for i in range(1, gridSize+1):
  grid[i][0] = 1
  grid[0][i] = 1
for i in range(1, gridSize+1):
  for j in range(1, gridSize+1):
    grid[i][j] = grid[i-1][j] + grid[i][j-1]
print(grid[-1][-1])