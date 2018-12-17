termsgenerated = 10
terms=[]
firstdiff = []
for i in range(1,termsgenerated+1):
    a = i + 1
    terms.append(a)
for i in range(0,termsgenerated-1):
    a = terms[i+1] - terms[i]
    firstdiff.append(a)
print(terms)
print(firstdiff)
