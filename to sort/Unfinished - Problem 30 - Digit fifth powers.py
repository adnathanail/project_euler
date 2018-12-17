for i in range(0,6):
    for j in range(0,6):
        for k in range(0,6):
            for l in range(0,6):
                num = str(i)+str(j)+str(k)+str(l)
                sofp = (i**5)+(j**5)+(k**5)+(l**5)
                if int(num) == sofp:
                    print(num+" = "+ str(i) + "**5 + " + str(j) + "**5 + " + str(k) + "**5 + " + str(l) + "**5")
