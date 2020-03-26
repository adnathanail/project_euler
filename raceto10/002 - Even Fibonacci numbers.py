i = 1
j = 1
tot = 0 # Starts at 0 because we're ignoring the first 2 terms because they're odd
while j < 4000000:
  i, j = j, i+j
  if j % 2 == 0:
    tot += j
print(tot)