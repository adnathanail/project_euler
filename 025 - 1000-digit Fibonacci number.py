fibs = [1,1]
lll = 0
while lll < 1000:
    fibs.append(fibs[-1]+fibs[-2])
    if len(str(fibs[-1])) > lll:
        lll = len(str(fibs[-1]))
print(len(fibs))
