alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
names=open('names.txt', 'r').read().split('","')
names.sort()

scores=[]

for name in names:
    score = 0
    for letter in name:
        score += alphabet.index(letter.lower())+1
    score *= names.index(name) + 1
    scores.append(score)
print(sum(scores))
