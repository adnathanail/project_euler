cubes = []
for c in range(10000):
  cubes.append(c**3)

isAnagram = lambda a, b: sorted(a) == sorted(b)

for i in range(len(cubes)):
  anagrams = [cubes[i]]
  for j in range(i+1, len(cubes)):
    if isAnagram(str(cubes[i]), str(cubes[j])):
      anagrams.append(cubes[j])
  if len(anagrams) == 5:
    print(anagrams)