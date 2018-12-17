termsgenerated = 10
terms=[]
firstdiff = []
seconddiff = []
for i in range(1,termsgenerated+1):
    a = (2*(i**2)) + i + 1
    terms.append(a)
for i in range(0,termsgenerated-1):
    a = terms[i+1] - terms[i]
    firstdiff.append(a)
for i in range(0,termsgenerated-2):
    a = firstdiff[i+1] - firstdiff[i]
    seconddiff.append(a)
print(terms)
print(firstdiff)
print(seconddiff)
