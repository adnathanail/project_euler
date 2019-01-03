cache = {}
def wtm(f, t): # Ways to make(from, to)
  if (t-f) in cache:
    return cache[t-f]
  # print(t-f)
  o = set()
  for d in [1,2,5,10,20,50,100,200]:
    if (f+d) < t:
      gfs = wtm(f+d,t)
      # print(gfs, f, t, d)
      for v in gfs:
        # print(v)
        q = list(v)
        # print(q)
        q.append(d)
        # print(q)
        r = tuple(sorted(q))
        # print(v,q,r)
        o.add(r)
    if (f+d) == t:
      o.add(tuple([d]))
  cache[t-f] = o
  # print(cache)
  return o

# print(wtm(0, 1))
# print(wtm(0, 2))
# print(wtm(0, 5))
print(len(wtm(0, 200)))