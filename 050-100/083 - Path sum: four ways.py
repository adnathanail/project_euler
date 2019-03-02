import pathlib
import networkx as nx

with open(pathlib.Path(__file__).parent / '081_matrix.txt') as f:
  grid = [[int(y) for y in x.split(",")] for x in f.read().split("\n") if x != '']
width = len(grid[0])
height = len(grid)

DG = nx.DiGraph()
edges = []
for i in range(width):
  for j in range(height):
    for dx,dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
      x = i + dx
      y = j + dy
      if 0 <= x < width and 0 <= y < height:
        edges.append(((i,j), (x,y), grid[y][x]))
DG.add_weighted_edges_from(edges)

print(nx.dijkstra_path_length(DG, (0,0), (width-1, height-1)) + grid[0][0])