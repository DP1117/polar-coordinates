import math
from plot import polar_plot

#Integers to N
def toN(n):
    nums = []
    for i in range(0, n + 1):
        nums.append(i)
    polar_plot(nums, nums)


#Sieve of Eratosthenes
def prime_sieve(n):
    if n < 2:
        return [0]
    primes = [2]
    multiples = []
    for i in range(3, n, 2):
        if(not i in multiples):
            primes.append(i)
        k = 3
        while i * k < n:
            multiples.append(i * k)
            k += 2
    polar_plot(primes, primes)

#Fibonacci Sequence
def fib(n):
    if n == 1:
        return [1]
    seq = [1,1]
    for i in range(2, n):
        seq.append((seq[i - 2] + seq[i - 1]) % (2 * math.pi))
    polar_plot(seq, seq)
