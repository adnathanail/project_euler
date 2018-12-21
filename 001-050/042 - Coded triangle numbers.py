triangles = []
for triangle in range(1,21):
  number = 0
  for line in range(1,triangle+1):
    number+=line
  triangles.append(number)

scores=[]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
words=open('words.txt', 'r').read().split('","')
numtriang = 0
for word in words:
  score = 0
  for letter in word:
    score += alphabet.index(letter.lower())+1
  if score in triangles:
    numtriang+=1
print(numtriang)
