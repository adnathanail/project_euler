# --- MATHS ---
# Finding all numbers where len(i**n) <= n
# 10**i always has i+1 digits so i < 10

# n = 1
# while n <= len(str(9**n)):
#   n += 1
# print(n)
# Gives 22 therefore n < 22

k = 0
for n in range(1,22):
  for i in range(1,10):
    if len(str(i**n)) == n:
      print("%i^%i" % (i, n))
      k += 1
print(k)