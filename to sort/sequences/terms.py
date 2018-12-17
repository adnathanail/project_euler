from itertools import count
sequence="1*(n**4)"
termsgenerated = 10

terms=[]
diffs=[]
term=int(sequence[sequence.find("n**")+3:sequence.find("n**")+4])

for i in range(0,term+1):
    x=[]
    if i == 0:
        for n in range(1,termsgenerated+1):
            a=eval(sequence)
            x.append(a)
    else:
        for j in range(0,termsgenerated-i):
            a = terms[i-1][j+1] - terms[i-1][j]
            x.append(a)
    terms.append(x)

print(terms[-1][-1]/int(sequence[:1]))
