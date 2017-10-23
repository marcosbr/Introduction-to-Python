import numpy as np
import matplotlib.pyplot as plt
import random

def next_point(x0, y0):
    """Gerar o proximo ponto na Samambaia de Barnsley."""
    r = random.random()
    if r <= 0.02:
        x1 = 0.0
        y1 = 0.16*y0
    elif r <= 0.86:
        x1 = 0.85*x0 + 0.04*y0
        y1 = -0.04*x0 + 0.85*y0 + 1.6
    elif r <= 0.93:
        x1 = 0.2*x0 - 0.26*y0
        y1 = 0.23*x0 + 0.22*y0 + 1.6
    else:
        x1 = -0.15*x0 + 0.28*y0
        y1 = 0.26*x0 + 0.24*y0 + 0.44
    return x1, y1


N = 100000
X = np.zeros(N)
Y = np.zeros(N)
X[0] = 0.0; Y[0] = 0.0;
k = 1
for k in range(1, N):
    X[k], Y[k] = next_point(X[k-1], Y[k-1])
    k += 1

Nmin = 500
fig = plt.gcf()
fig.set_size_inches(6, 10)
ax = plt.axes(frameon=False)
ax.axes.get_xaxis().set_visible(False)  # remove the axes
ax.axes.get_yaxis().set_visible(False)
plt.plot(X[Nmin:], Y[Nmin:], ',', c='g')
plt.show()
