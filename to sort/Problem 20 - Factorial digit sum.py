num = 100
for i in range(1,num):
    num*=i
print(sum([int(x) for x in list(str(num))]))
