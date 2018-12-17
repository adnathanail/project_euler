def sumSquare(num):
    tot = 0
    for i in range(1,num+1):
        tot += i**2
    return tot
def squareSum(num):
    tot = 0
    for i in range(1,num+1):
        tot += i
    tot = tot**2
    return tot
print(squareSum(100)-sumSquare(100))
