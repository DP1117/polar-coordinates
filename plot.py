#Plotting
import matplotlib.pyplot as plt

def polar_plot(r, theta, area=1, show_grid=False):
    bg_color = '#000000'

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='polar')
    ax.set_yticklabels([])

    if not show_grid:
        ax.grid(False)
        ax.set_facecolor(bg_color)
        fig.patch.set_facecolor(bg_color)

    ax.scatter(theta, r, marker="o", s=area)
    plt.show()
