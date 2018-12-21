dividingBy = 20
dividing = 10599120
Over = False
while not(Over):
  for i in [11, 13, 14, 16, 17, 18, 19, 20]:
    if dividing%i:
      break
    else:
      print(str(dividing) + " was divisible by " + str(i))
      if i == 2:
        Over = True
  if not(Over):
    dividing += 2520
    print(str(dividing) + " is not divisble by every number from 1-" + str(dividingBy))
print(str(dividing) + " is divisible by 1")
print(str(dividing) + " is divisble by every number from 1-" + str(dividingBy))
