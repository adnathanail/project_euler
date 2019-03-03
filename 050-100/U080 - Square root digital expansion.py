from decimal import Decimal, getcontext

getcontext().prec = 105

def sqrt(x):
  left = 0
  right = x
  guess = (right+left)/2
  for enumber in range(1,100+1):
    # print(enumber, guess)
    epsilon = 1/(10**enumber)  
    while abs(guess**2-x) >= epsilon:
      if guess**2 < x:
        left = guess
      else:
        right = guess
      guess = (right+left)/2
  return guess

# for i in range(1,100):
#   print(sqrt(Decimal(i)))
# print(sqrt(Decimal(8)))

print(sqrt(Decimal(2)))

# tot = 0
# for i in range(1,100):
#   tot += sum([int(x) for x in str(sqrt(Decimal(i))).replace('.',"")[:100]])
# print(tot)
