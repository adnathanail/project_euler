import unittest


# def convex_path_a(n):
#   """ Only uses ratios of 1x1, 1x2, 1x3 etc."""
#   i = 1
#   tot = 0
#   while tot + i <= n:
#     tot += i
#     i += 1
#   return i


# In a 7x7 the ideal is:
# 3,1
# 2,1
# 1,1
# 1,2
# Or
# 2,1
# 1,1
# 1,2
# 1,3
# In a 6x6:
# 2,1
# 1,1
# 1,2
# The max of each direction is n
# 1,1 always needs to be at position n/2 or (n+-1)/2 (1-indexed)

# def convex_path(n):
#   """ Only uses ratios of 1x1, 1x2 etc. 2x1, 3x1, 4x1 etc."""
#   if n < 1:
#     return 0
#   num_shallow_paths = 1  # Number of ax1 paths
#   width_used = 0
#   while (width_used + num_shallow_paths) + (num_shallow_paths - 1) <= n:
#     width_used += num_shallow_paths
#     num_shallow_paths += 1
#   num_shallow_paths -= 1
#
#   height_used = num_shallow_paths
#   num_steep_paths = 0
#   if height_used + 2 <= n:
#     num_steep_paths = 1
#     while (height_used + num_steep_paths + 1) <= n:
#       height_used += num_steep_paths + 1
#       num_steep_paths += 1
#     num_steep_paths -= 1
#   return num_shallow_paths + num_steep_paths + 1  # Number of points is number of paths + 1


# Turns out this is secretly a problem about fractions
# The second attempt works up to 9 but for 11 it misses out 3/2 between 1/1 and 2/1
# 11 should be:
# 1/3, 1/2, 1/1, 3/2, 2/1, 3/1
# The numerators and denominators all have to add to n

# There's something to do with the "simplest ratio with the smallest num/dom"
# e.g. for some larger value of n I think 5/2 will come in between

# Minimize the each numerator + denominator!

def generate_sum_pairs(n):
  """
    Generates all pairs summing to n (where each item in the pair > 0)
    Ordered in increasing "unbalance" of numerator and denominator
    i.e. n = 6 -> [(3, 3), (2, 4), (4, 2), (1, 5), (5, 1)]
  """
  out = []
  for i in range((n // 2), 0, -1):
    out.append((i, n-i))
    if i != n - i:
      out.append((n-i, i))
  return out


def gcd(a, b):
  while a > 0:
    a, b = b % a, a
  return b


def simplify_sum_pairs(sum_pairs):
  out = []
  for pair in sum_pairs:
    pair_gcd = gcd(pair[0], pair[1])
    out.append((pair[0] // pair_gcd, pair[1] // pair_gcd))
  return out


def convex_path(n):
  num_tot = 0
  den_tot = 0
  num_paths = 0

  pair_total_max = 2
  pairs_used = []
  pair_used_this_round = True
  while num_tot < n and den_tot < n and pair_used_this_round:
    pair_used_this_round = False
    pairs = simplify_sum_pairs(generate_sum_pairs(pair_total_max))
    for pair in pairs:
      if pair in pairs_used:
        continue
      if num_tot + pair[0] <= n and den_tot + pair[1] <= n:
        num_tot += pair[0]
        den_tot += pair[1]
        num_paths += 1
        pair_used_this_round = True
      pairs_used.append(pair)
    pair_total_max += 1
  return num_paths + 1  # Number of points = number of paths + 1


# The third attempt is (i believe) fully correct but now too inefficient to manage 10^18


class ConvexPathTests(unittest.TestCase):
  def test_visually(self):
    for i in range(1, 20):
      print(i, convex_path(i))
    _ = self

  def test_against_provided_values(self):
    vals = {1: 2, 3: 3, 9: 6, 11: 7, 100: 30, 50000: 1898}
    for k in vals:
      self.assertEqual(convex_path(k), vals[k])
