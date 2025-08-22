import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def make(a, b, c, r):
    database = open("database_sphere.txt", "r")

    xAxis_array = []
    yAxis_array = []
    zAxis_array = []
    lines = 0

    for line in database:
        dataLine = line.strip().split(" ")
        xAxis_array.append(float(dataLine[0]))
        yAxis_array.append(float(dataLine[1]))
        zAxis_array.append(float(dataLine[2]))
        lines += 1

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    for i in range(lines):
        x = xAxis_array[i]
        y = yAxis_array[i]
        z = zAxis_array[i]
        ax.scatter(x, y, z, c="r")
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = a + r * np.outer(np.cos(u), np.sin(v))
    y = b + r * np.outer(np.sin(u), np.sin(v))
    z = c + r * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, color = (97/256, 255/256, 250/256), rcount = 20, ccount = 30, alpha = 0.3,
                    shade = False)
    ax.set_aspect('equal')
    # ax.set_title('SPHERE DETECT', loc = 'left')
    s = f"(X-{a:.2f})^2 + (Y-{b:.2f})^2 + (Z-{c:.2f})^2 = {r:.2f}^2"
    ax.set_title(s, loc = 'center')
    plt.show()