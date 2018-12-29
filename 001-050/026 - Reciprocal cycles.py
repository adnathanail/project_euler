def div(a, b): # a/b
  # zz = a
  dividings = [a]
  o = str(a//b) + "."
  a = a%b * 10
  while a not in dividings and a != 0:
    dividings.append(a)
    o += str(a//b)
    a = a%b * 10
  l = list(o)
  i = 2 if str(a//b) == "0" else l.index(str(a//b))
  k = len(l)-i
  
  # if a == 0:
  #   o = "".join(l)
  # else:
  #   l.insert(i, "(")
  #   o = "".join(l) + ")"
  # print("%i/%i %f" % (zz,b, zz/b), k, o)
  return k

longest_length = 0
longest_num = 0
for i in range(2,1000):
  z = div(1,i)
  if z > longest_length:
    longest_num, longest_length = i, z
print(longest_num)