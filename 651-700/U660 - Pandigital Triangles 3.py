def gcd(a,b) :
  while b!=0:
    a,b = b, a%b
  return a

def tobase(n,b):
  "return the decomposition of n>0 in base b (list)"
  l = list()
  while n>0:
    l.append(n%b)
    n //=b
  return l[::-1]

s = 0
u,ustop = 0,False
while not ustop: # loop on u
  u += 1
  v,vstop = u,False
  while not vstop: # loop on v
    v += 1
    if gcd(u,v)==1 and (u-v)%3!=0:
      p0 = v**2-u**2
      q0 = u*(u+2*v)
      r0 = v**2+u*v+u**2
      d,dstop = 1,False
      while not dstop: # loop on d (common factor)
        p,q,r = d*p0,d*q0,d*r0
        for b in range(9,19): # base
          L = tobase(p,b)+tobase(q,b)+tobase(r,b)
          if len(L)==b==len(set(L)):
            print(r)
            s += r # update sum 
        if len(L)>b: 
          if d==1:
            vstop = True
            if v==u+1:
              ustop = True
          dstop = True
        d += 1
print(s)