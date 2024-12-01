def get_numbers_containing_zeroes():
    """
    Generate all numbers containing zeroes in order.
    These act as our "templates" for creating our potential prime sets
    """
    i = 10

    while True:
        istr = str(i)
        lenistr = len(istr)
        # If we have only 1 0, increment the first non-zero digit starting from the right (smallest place value)
        if istr.count("0") == 1:
            # If we have just 1 0, then it will either be the last value, in which case we increment the second to last value
            if istr[-1] == "0":
                i += 10
            # Or it will be somewhere else, and we just increment the last value
            else:
                i += 1
        # Otherwise if the last digit is zero we increment that
        elif istr[-1] == "0":
            i += 1
        # Otherwise we increment the first digit after we find a zero starting from the right (smallest place value)
        else:
            for k in range(lenistr - 1, -1, -1):
                if istr[k] != "0":
                    break
            # Convert string index of first zero digit, to the place value of the column
            # e.g. 100,    k = 2, num_to_add = 1
            #      400334, k = 2, num_to_add = 1000
            num_to_add = 10 ** (lenistr - k - 1)
            i += num_to_add
        yield istr


SINGLE_DIGIT_STRINGS = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
def generate_nums_from_template(template):
    """
    Given a template like 1003, return the 10 possible replacements:
    1003, 1113, 1223, 1333, 1443, 1553, 1663, 1773, 1883, 1993
    """
    return [int(template)] + [int(template.replace("0", i)) for i in SINGLE_DIGIT_STRINGS]


class SieveOfEratosthenes:
    """
    Prime checker which doesn't forget its previous results, so it can be efficiently used lots of times
    """
    def __init__(self):
        self.primes = [True, False, True] # Using 1-indexing
        self.current_max_prime = 2

    def isprime(self, n):
        if n < 2:
            return False
        self.primes += [True for _ in range(n - self.current_max_prime)]

        p = self.current_max_prime
        newp = True
        while newp:
            for i in range(p*p, n + 1, p):
                self.primes[i] = False
            
            newp = False
            for i in range(p + 1, n):
                if self.primes[i]:
                    p = i
                    newp = True
                    break

        return self.primes[n]


gen = get_numbers_containing_zeroes()
sieve = SieveOfEratosthenes()


current_record_num_primes = 0
current_record_num_primes_prime = -1

for i in range(200):
    template = next(gen)
    print("\t", template)
    potential_primes = generate_nums_from_template(template)
    num_primes = len([p for p in potential_primes if sieve.isprime(p)])
    if num_primes > current_record_num_primes:
        current_record_num_primes = num_primes
        current_record_num_primes_prime = min(potential_primes)
        print(current_record_num_primes_prime, current_record_num_primes)
    # print(min(potential_primes), len([p for p in potential_primes if sieve.isprime(p)]))
