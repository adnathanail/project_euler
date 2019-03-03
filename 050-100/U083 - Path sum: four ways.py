import pathlib, sys
from math import inf

# sys.setrecursionlimit(10000)

with open(pathlib.Path(__file__).parent / '081_matrix.txt') as f:
  grid = [[int(y) for y in x.split(",")] for x in f.read().split("\n") if x != '']
width = len(grid[0])
height = len(grid)

def flatten(l):
  return [i for s in l for i in s]

xys = [str(j)+str(i) for j in range(width) for i in range(height)]
distance_matrix = {a:{b:inf for b in xys} for a in xys}
visited = []
# print(distance_matrix)
# distances = []

# for row in grid:
#   print(row)
# print()

def distance(grid, f, t, visited=[]):
  # print(f, t, visited)
  val = grid[f[1]][f[0]]
  if f == t:
    return val
  # visited.append(f)
  options = []
  for x,y in [[f[0]-1,f[1]], [f[0]+1,f[1]], [f[0],f[1]-1], [f[0],f[1]+1]]:
    if 0 <= x < width and 0 <= y < height and [x,y] not in visited:
      # print(1)
      d = distance(grid,[x,y],t,visited + [f])
      if d is not None:
        options.append(d)
  #   # print(x,y)
  # if len(options) == 0:
  #   dead.append(f)
  #   print(min(options), f, t, visited)
  return min(options) + val if len(options) > 0 else None

print(distance(grid,[0,0],[width-1,height-1]))





# import pathlib, sys
# from math import inf

# with open(pathlib.Path(__file__).parent / '082_matrix.txt') as f:
#   grid = [[int(y) for y in x.split(",")] for x in f.read().split("\n") if x != '']
# width = len(grid[0])
# height = len(grid)

# def distance(grid, f, t, visited=[]):
#   val = grid[f[1]][f[0]]
#   if f == t:
#     return val
#   options = []
#   for x,y in [[f[0]-1,f[1]], [f[0]+1,f[1]], [f[0],f[1]-1], [f[0],f[1]+1]]:
#     if 0 <= x < width and 0 <= y < height and [x,y] not in visited:
#       d = distance(grid,[x,y],t,visited + [f])
#       if d is not None:
#         options.append(d)
#   return min(options) + val if len(options) > 0 else None

# print(distance(grid,[0,0],[width-1,height-1]))