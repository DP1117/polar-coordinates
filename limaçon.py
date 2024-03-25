import math
from plot import polar_plot

def limacon(a, b):
    radii = []
    thetas = []
    theta = 0
    while theta <= math.pi * 2:
        radii.append(r(a, b, theta))
        thetas.append(theta)
        theta += 0.1
    polar_plot(radii, thetas)

# r = a ± b*cos(θ)
def r(a, b, theta):
    return a + b * math.cos(theta)