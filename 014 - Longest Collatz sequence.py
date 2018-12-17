def collatz(n,t):
	t += 1
	if n == 1:
		return t
	if n%2 == 0:
		n = int(n/2)
	else:
		n = int(3*n +1)
	return collatz(n,t)

biggest = 0
biggest_length = 0
for i in range(1,1000000):
    if i % 10000 == 0:
        print(i)
    c = collatz(i,0)
    if c > biggest_length:
        biggest = i
        biggest_length = c
print(biggest, biggest_length)
        
