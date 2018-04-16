import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D

def f(x, y):
    return 3*x*y

x = np.linspace(0, 6, 30)
y = np.linspace(0, 6, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = Axes3D(fig)
ax.contour3D(X, Y, Z, 500, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z');

ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
fig.savefig('3xy-1.png')
