primes = []
for i in range(2,200000):
	prime = True
	for prime in primes:
		if prime > i/2:
			break
		else:
			if i % prime == 0:
				prime = False
				break
	if prime:
		primes.append(i)
	if len(primes) == 10001:
		break
print(primes[-1])
