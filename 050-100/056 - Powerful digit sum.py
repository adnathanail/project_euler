digitalsum = []
for a in range(1,101):
  for b in range(1,101):
    digitalsum.append(sum(int(digit) for digit in str(a**b)))
print(max(digitalsum))
