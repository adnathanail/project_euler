import pathlib

with open(pathlib.Path(__file__).parent / '081_matrix.txt') as f:
  grid = [[int(y) for y in x.split(",")] for x in f.read().split("\n") if x != '']
width = len(grid[0])
height = len(grid)

for x in range(width-2,-1,-1):
  checking_above = [0 for q in range(height)]
  checking_below = [0 for q in range(height)]
  for y in range(height):
    ca_options = []
    if (x+1) < width:
      ca_options.append(grid[y][x+1])
    if -1 < (y-1) < height:
      ca_options.append(checking_above[y-1])
    checking_above[y] = grid[y][x] + min(ca_options) if len(ca_options) > 0 else 0
  for y in range(height-1,-1,-1):
    cb_options = []
    if (x+1) < width:
      cb_options.append(grid[y][x+1])
    if (y+1) < height:
      cb_options.append(checking_below[y+1])
    checking_below[y] = grid[y][x] + min(cb_options) if len(cb_options) > 0 else 0
  for y in range(height):
    options = [checking_above[y], checking_below[y]]
    grid[y][x] = min(options)

print(min([l[0] for l in grid]))