import math
from plot import polar_plot

def two_theta():
    x_theta(2)

def three_theta():
    x_theta(3)

def x_theta(x):
    radii = []
    thetas = []
    theta = 0
    while theta < math.pi * 2:
        radii.append(math.cos(x * theta))
        thetas.append(theta)
        theta += 0.05
    polar_plot(radii, thetas)