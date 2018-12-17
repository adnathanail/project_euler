gridSize = 20
grid = []
for i in range(gridSize+1):
    grid.append([])
    for j in range(gridSize+1):
        grid[-1].append(0)
for i in range(gridSize):
    grid[i][gridSize] = 1
    grid[gridSize][i] = 1
for i in range(gridSize-1,-1,-1):
    for j in range(gridSize-1,-1,-1):
        grid[i][j] = grid[i+1][j] + grid[i][j+1]

for row in grid:
    print(row)
