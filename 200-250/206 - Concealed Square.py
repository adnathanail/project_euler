# 1_2_3_4_5_6_7_8_9_0 is a 19 digit number
# If the last digit is 0 it is divisible by 10
# If it is square it must be divisible by 10 twice so the last missing value is 0
# 1_2_3_4_5_6_7_8_900 = 1_2_3_4_5_6_7_8_9 * 10^2
# The only numbers which when squared give a 9 end in 3 or 7
# Therefore the second to last number of the root is 3 or 7
# 03^2, 13^2 etc and 07^2, 17^2 etc only ever have an even number as the second to last digit of their square
# Therefore h is always even (0,2,4,6,8)
from decimal import Decimal

def is_the_one(n):
  s = str(n)
  return s[0] == "1" and s[2] == "2" and s[4] == "3" and s[6] == "4" and s[8] == "5" and s[10] == "6" and s[12] == "7" and s[14] == "8" and s[16] == "9" and s[18] == "0"

def is_square(n):
  return n.sqrt()%1==0

def find_the_one():
  for a in range(9,-1,-1): # Reverse-order because... it finds it quicker
    for b in range(9,-1,-1):
      for c in range(9,-1,-1):
        print(a,b,c)
        for d in range(10):
          for e in range(10):
            for f in range(10):
              for g in range(10):
                for h in [0,2,4,6,8]:
                  n = Decimal(10**18 + a*(10**17) + 2*(10**16) + b*(10**15) + 3*(10**14) + c*(10**13) + 4*(10**12) + d*(10**11) + 5*(10**10) + e*(10**9) + 6*(10**8) + f*(10**7) + 7*(10**6) + g*(10**5) + 8*(10**4) + h*(10**3) + 900)
                  if is_square(n):
                    return n.sqrt()

print(find_the_one())