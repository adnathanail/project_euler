import pathlib
from copy import deepcopy

grids = []
with open(pathlib.Path(__file__).parent / '096_sudoku.txt') as f:
  lines = f.read().split('\n')
  for i in range(int(len(lines)/10)):
    grids.append([list(map(int,list(l))) for l in lines[i*10+1:i*10+10]])

def can_go_here(grid, x, y, n):
  xgroup = [0,1,2] if 0 <= x < 3 else [3,4,5] if 3 <= x < 6 else [6,7,8]
  ygroup = [0,1,2] if 0 <= y < 3 else [3,4,5] if 3 <= y < 6 else [6,7,8]
  for tx in xgroup:
    for ty in ygroup:
      if grid[ty][tx] == n:
        return False
  return n not in [grid[y][i] for i in range(9)] and n not in [grid[i][x] for i in range(9)]

def possibilities(grid, x, y):
  return [n for n in range(1,9+1) if can_go_here(grid, x, y, n)]

def solve(grid):
  grid = deepcopy(grid)

  # Try and solve with simple logic
  change_made = True
  while change_made:
    change_made = False
    snop = 100000 # Smallest number of possibilities
    snopp = [] # snop possibilities
    for x in range(9):
      for y in range(9):
        if grid[y][x] != 0:
          continue
        ps = possibilities(grid, x, y)
        if len(ps) < 1:
          return None
        elif len(ps) == 1:
          grid[y][x] = ps[0]
          change_made = True
        else:
          if len(ps) < snop:
            snop = len(ps)
            snopp = [x,y, ps]
  
  # Solve remainder by brute-forcing individual digits and attempting logic again
  # Recursive so eventually will be solved even if just by brute-force
  if any([0 in l for l in grid]):
    for p in snopp[2]:
      grid[snopp[1]][snopp[0]] = p
      g = solve(grid)
      if g:
        return g
      else:
        grid[snopp[1]][snopp[0]] = 0
    return None
  else:
    return grid

print(sum([int("".join(list(map(str,solve(grid)[0][:3])))) for grid in grids]))