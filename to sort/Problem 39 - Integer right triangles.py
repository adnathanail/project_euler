import itertools
import operator

def most_common(L):
  # get an iterable of (item, iterable) pairs
  SL = sorted((x, i) for i, x in enumerate(L))
  # print 'SL:', SL
  groups = itertools.groupby(SL, key=operator.itemgetter(0))
  # auxiliary function to get "quality" for an item
  def _auxfun(g):
    item, iterable = g
    count = 0
    min_index = len(L)
    for _, where in iterable:
      count += 1
      min_index = min(min_index, where)
    # print 'item %r, count %r, minind %r' % (item, count, min_index)
    return count, -min_index
  # pick the highest-count/earliest item
  return max(groups, key=_auxfun)[0]

from math import sqrt
limit = 1000
triples = []
values = []
for a in range(1,limit+1):
    for b in range(a+1,limit+1):
        c = sqrt((a**2)+(b**2))
        if c.is_integer() and not([a,b,int(c)] in triples):
            print("a: " + str(a) + " b: " + str(b) + " c: " + str(int(c)))
            triples.append([a,b,int(c)])
        if (a+b+c) > limit:
            break
for triple in triples:
    values.append(sum(triple))
print(most_common(values))
