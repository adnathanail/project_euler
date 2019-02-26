def is_prime(n):
  for i in range(2,int(n**0.5)+1):
    if not n%i:
      return False
  return True

def is_anagram(a,b):
  return sorted(str(a)) == sorted(str(b))

for i in range(1001,9999,2):
  if is_prime(i):
    for d in range(1,9999-i):
      if is_prime(i+d) and is_prime(i+2*d):
        if is_anagram(i,i+d) and is_anagram(i,i+2*d):
          print(i,d)
          print(str(i) + str(i+d) + str(i+2*d))
print("Primes generated")
