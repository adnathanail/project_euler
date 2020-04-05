sbf = {}

def collatz(n):
	if n == 1:
		return 1
	n = int(3*n +1) if n%2 else int(n/2)
	if n not in sbf:
		sbf[n] = collatz(n)
	return sbf[n] + 1

biggest = 0
biggest_length = 0
for i in range(1,1000000):
	c = collatz(i)
	if c > biggest_length:
		biggest = i
		biggest_length = c

print(biggest)