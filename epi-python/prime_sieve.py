from typing import List


def generate_primes(n: int) -> List[int]:
    # is_prime[i] describes if i is prime or not
    # is_prime is initially set to [False, False, True, True, True, ...] (n + 1 many times)
    #                               0       1       2     3     4   ...
    #                               0 is not prime,
    #                               1 is not prime,
    #                               2 is prime

    is_prime = [False, False] + [True] * (n - 1)

    answer = []
    # Then from this initial state, we check if 2 and greater is prime or not
    for p in range(2, n + 1):
        if is_prime[p]:  # if p is prime,
            answer.append(p)  # 1. append to answer (obivious)
            for i in range(
                p * 2, n + 1, p
            ):  # 2. mark all of its multiples as non-prime
                is_prime[i] = False
    # then finally we return the answer
    return answer


# A faster way is to mark all even numbers as non-prime, except 2.
# This is because we know that all even numbers are divisible by 2 (excluding 2), hence they can't be prime
# Therefore, we just check for the odd numbers
def generate_primes2(n: int) -> List[int]:
    # Since we want to have 2 in the answer list as an initial state (for reason below later), we need to check if n is < 2
    # if yes, then just return an empty list (i.e. theres no prime that is smaller than 2)
    if n < 2:
        return []

    # in discrete math, we can express even numbers as 2i and odd numbers as 2i + 1 because:
    # - An even number is any integer that is divisible by 2 where i is any integer (... -2, -1, 0, 1, 2 ...)
    # - An odd number is one more than an even number where i is any integer (... -2, -1, 0, 1, 2 ...)

    size = (n - 3) // 2 + 1  # where did we get this??
    # We want all 2i + 3 ≤ n.
    # Solve for i:
    # 2i + 3 ≤ n
    # 2i ≤ n - 3
    # i ≤ (n - 3) // 2
    is_prime = [True] * size
    answer = [2]  # because we know 2 is a prime, we can always set that to true

    for p in range(size):
        if is_prime[p]:
            prime = p * 2 + 3
            answer.append(prime)
            for i in range(2 * p**2 + 6 * p + 3, size, prime):  # why??
                is_prime[i] = False

    # This is a modified Sieve of Eratosthenes that only tracks odd numbers.
    # When you find a prime number p = 2i + 3, you want to mark all its multiples as not prime starting from p².
    # But is_prime only represents odd numbers, so we need to map p² (an odd number) back to the correct index in the is_prime array.

    # We want to start sieving at p²
    # p² = (2i + 3)² = 4i² + 12i + 9
    # Now map p² to an index j in is_prime, which represents values of form 2j + 3.
    #   2j + 3 = 4i² + 12i + 9
    # → 2j = 4i² + 12i + 6
    # → j = 2i² + 6i + 3
    # start_index = 2 * i**2 + 6 * i + 3

    return answer


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    is_prime = [False, False] + [True] * (n - 1)
    primes = []
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    # print(is_prime)

    return primes
