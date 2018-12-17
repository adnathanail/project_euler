collatzes=[]
def even(num):
    return num/2
def odd(num):
    return (3*num)+1
def collatz(num):
    counter = 0
    while num != 1:
        if num%2:
            num = odd(num)
        else:
            num = even(num)
        counter += 1
    return counter
for i in range(1,1000000):
    collatzes.append(collatz(i))
    print(str(i)+": " + str(collatz(i)))
