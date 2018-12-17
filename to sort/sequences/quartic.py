termsgenerated = 10
terms=[]
firstdiff = []
seconddiff = []
thirddiff = []
fourthdiff = []
for i in range(1,termsgenerated+1):
    a = (4*(i**4)) + (3*(i**3)) + (2*(i**2)) + i + 1
    terms.append(a)
for i in range(0,termsgenerated-1):
    a = terms[i+1] - terms[i]
    firstdiff.append(a)
for i in range(0,termsgenerated-2):
    a = firstdiff[i+1] - firstdiff[i]
    seconddiff.append(a)
for i in range(0,termsgenerated-3):
    a = seconddiff[i+1] - seconddiff[i]
    thirddiff.append(a)
for i in range(0,termsgenerated-4):
    a = thirddiff[i+1] - thirddiff[i]
    fourthdiff.append(a)
print(terms)
print(firstdiff)
print(seconddiff)
print(thirddiff)
print(fourthdiff)
