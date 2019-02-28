import pathlib

with open(pathlib.Path(__file__).parent / '081_matrix.txt') as f:
  grid = [[int(y) for y in x.split(",")] for x in f.read().split("\n") if x != '']
width = len(grid[0])
height = len(grid)

for y in range(height-1,-1,-1):
  for x in range(width-1,-1,-1):
    options = []
    try:
      options.append(grid[y][x+1])
    except IndexError:
      pass
    try:
      options.append(grid[y+1][x])
    except IndexError:
      pass
    cheapest = 0
    try:
      cheapest = min(options)
    except ValueError:
      pass
    grid[y][x] = grid[y][x] + cheapest

print(grid[0][0])