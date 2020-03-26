# a + b + c = 1000
# a, b, c != 0
# Therefore a and b are each at most 998
def get_triple_equal_to(n):
  for a in range(1, n-2+1):
    for b in range(1, n-2+1):
      if (c := (a**2 + b**2)**0.5).is_integer():
        if sum([a, b, c]) == n:
          return a * b * c
print(get_triple_equal_to(1000))