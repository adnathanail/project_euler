import math

import numpy as np


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


class PersistentSieve:
    """
    Prime number sieve that remembers and efficiently stores all previously found primes
    """

    def __init__(self):
        # Initial small primes to bootstrap the sieve
        self.known_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        self.primes_set = set(self.known_primes)
        self.max_checked = max(self.known_primes)

        # Use a compact bit array to track prime status
        self.prime_flags = np.ones(max(self.known_primes) * 2 + 1, dtype=np.bool_)
        self.prime_flags[0:2] = False

        # Mark known composites
        for p in self.known_primes[1:]:  # Skip 2
            self.prime_flags[p * p::p] = False

    def _extend_sieve(self, n):
        """
        Extend the sieve to cover numbers up to n while preserving existing information
        """
        if n <= self.max_checked:
            return

        # Exponential growth with a cap to prevent excessive memory use
        new_max = min(n * 2, max(n * 1.5, self.max_checked * 2))
        new_max = int(new_max)

        # Resize prime_flags if needed
        if new_max >= len(self.prime_flags):
            # Create a new, larger array and copy existing flags
            new_flags = np.ones(new_max + 1, dtype=np.bool_)
            new_flags[:len(self.prime_flags)] = self.prime_flags
            self.prime_flags = new_flags

        # Efficient sieving
        sqrt_max = int(math.sqrt(new_max)) + 1
        for p in self.known_primes:
            if p > sqrt_max:
                break

            # Start marking from the first multiple of p not already marked
            start = max(p * p, ((self.max_checked // p) + 1) * p)
            self.prime_flags[start:new_max + 1:p] = False

        # Find and store new primes
        new_primes = [x for x in range(self.max_checked + 1, new_max + 1)
                      if self.prime_flags[x]]

        self.known_primes.extend(new_primes)
        self.primes_set.update(new_primes)
        self.max_checked = new_max

    def isprime(self, n):
        """
        Efficiently check if a number is prime
        """
        # Quick checks for known primes
        if n in self.primes_set:
            return True

        # Quick composite check for known small primes
        for p in self.known_primes:
            if p * p > n:
                break
            if n % p == 0:
                return False

        # Extend sieve if needed
        self._extend_sieve(n)

        return bool(self.prime_flags[n])


gen = get_numbers_containing_zeroes()
sieve = PersistentSieve()

current_record_num_primes = 0
current_record_num_primes_prime = -1

for i in range(1000000):
    template = next(gen)
    potential_primes = generate_nums_from_template(template)
    num_primes = len([p for p in potential_primes if sieve.isprime(p)])
    if num_primes > current_record_num_primes:
        current_record_num_primes = num_primes
        current_record_num_primes_prime = min(potential_primes)
        print(current_record_num_primes_prime, current_record_num_primes)
    # print(min(potential_primes), len([p for p in potential_primes if sieve.isprime(p)]))

# 10 4
# 101 5
# 107 6
# 56003 7
# 2090021 8
