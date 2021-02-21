# import math

# def generate_swaps(n):
#   num_digits = int(math.log10(n))+1
#   for i in range(num_digits):
#     pot = 10 ** i
#     n_truncated_from_left = n % (pot * 10)
#     n_truncated_from_both_sides = n_truncated_from_left // pot
#     n_without_ith_digit = n - (n_truncated_from_both_sides * pot)
#     print(n_without_ith_digit)

# generate_swaps(2567)

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

def isprime(n):  # TODO speed up
  if n < 2:
    return False
  primes = [True for _ in range(n + 1)]

  p = 2
  newp = True
  while newp:
    for i in range(p*p, n + 1, p):
      primes[i] = False
    
    newp = False
    for i in range(p + 1, n):
      if primes[i - 1]:
        p = i
        newp = True
        break

  return primes[n]

if __name__ == "__main__":
  biggest_i = 0
  biggest_i_template = ""
  for template in generate_templates(5):
    nums = generate_nums_from_template(template)
    i = 0
    for n in nums:
      if isprime(n):
        i += 1
    if i > biggest_i:
      biggest_i = i
      biggest_i_template = template
  print(biggest_i, biggest_i_template)