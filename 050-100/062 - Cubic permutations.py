cubes = []
for c in range(10000):
  cubes.append(sorted(str(c**3)))


for i in range(len(cubes)):
  anagrams = [i**3]
  for j in range(i+1, len(cubes)):
    if cubes[i] == cubes[j]:
      anagrams.append(j**3)
  if len(anagrams) == 5:
    print(anagrams)