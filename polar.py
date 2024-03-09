# Plotting
import matplotlib.pyplot as plt
import math

def polar_plot(r, theta, area=1, show_grid=False):
    bg_color = '#000000'

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='polar')
    ax.set_yticklabels([])

    if not show_grid:
        ax.grid(False)
        ax.set_facecolor(bg_color)
        fig.patch.set_facecolor(bg_color)

    ax.scatter(r, theta, marker="o", s=area)
    plt.show()

# Sieve of Eratosthenes
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


num_points = 10
max_points = 100000
while num_points <= max_points:
    fib(num_points)
    num_points *= 10