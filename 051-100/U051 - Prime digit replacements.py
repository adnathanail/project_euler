NUMS = ["*", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def generate_templates(longest_template):
  if longest_template < 1:
    return []
  elif longest_template == 1:
    return NUMS
  out = []
  for shorter in generate_templates(longest_template - 1):
    for num in NUMS:
      out.append(num + shorter)
  return out

def generate_nums_from_template(template):
  out = set()
  for i in range(10):
    out.add(template.replace("*", str(i)))
  return [int(n) for n in out if n[0] != "0"]

class SieveOfEratosthenes:
  def __init__(self):
    self.primes = [True, False, True] # Using 1-indexing
    self.current_max_prime = 2

  def isprime(self, n):
    if n < 2:
      return False
    self.primes += [True for _ in range(n - self.current_max_prime)]

    p = self.current_max_prime
    newp = True
    while newp:
      for i in range(p*p, n + 1, p):
        self.primes[i] = False
      
      newp = False
      for i in range(p + 1, n):
        if self.primes[i]:
          p = i
          newp = True
          break

    return self.primes[n]

if __name__ == "__main__":
  sieve = SieveOfEratosthenes()
  biggest_i = 0
  biggest_i_template = ""
  for template in generate_templates(5):
    nums = generate_nums_from_template(template)
    i = 0
    for n in nums:
      if sieve.isprime(n):
        i += 1
    if i > biggest_i:
      biggest_i = i
      biggest_i_template = template
  print(biggest_i, biggest_i_template)
