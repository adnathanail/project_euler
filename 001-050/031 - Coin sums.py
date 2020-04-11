cache = {}
def wtm(f, t): # Ways to make(from, to)
  if (t-f) in cache:
    return cache[t-f]
  o = set()
  for d in [1,2,5,10,20,50,100,200]:
    if (f+d) < t:
      gfs = wtm(f+d,t)
      for v in gfs:
        q = list(v)
        q.append(d)
        r = tuple(sorted(q))
        o.add(r)
    if (f+d) == t:
      o.add(tuple([d]))
  cache[t-f] = o
  return o

print(len(wtm(0, 200)))