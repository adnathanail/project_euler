import pathlib

with open(pathlib.Path(__file__).parent / '081_matrix.txt') as f:
  grid = [[int(y) for y in x.split(",")] for x in f.read().split("\n") if x != '']
width = len(grid[0])
height = len(grid)

for x in range(width-1,-1,-1):
  for y in range(height-1,-1,-1):
    options = []
    if (x+1) < len(grid[y]):
      options.append(grid[y][x+1])
    if (y+1) < len(grid):
      options.append(grid[y+1][x])
    cheapest = min(options) if len(options) > 0 else 0
    grid[y][x] = grid[y][x] + cheapest

print(grid[0][0])