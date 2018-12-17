totstr = ""
i = 1
while len(totstr) < 1000000:
    totstr = totstr + str(i)
    i += 1
print(int(totstr[1-1]) * int(totstr[10-1]) * int(totstr[100-1]) * int(totstr[1000-1]) * int(totstr[10000-1]) * int(totstr[100000-1]) * int(totstr[1000000-1]))
