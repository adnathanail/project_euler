tot = 1
dim = 1001
for i in range(1,int((dim-1)/2)+1):
    tot += 4*i**2 - 2*i + 1
    tot += 4*i**2 + 1
    tot += 4*i**2 + 2*i + 1
    tot += 4*i**2 + 4*i + 1
print(tot)
