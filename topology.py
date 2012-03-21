import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Line3D
import matplotlib.pyplot as plt
import matplotlib.lines as lines

def randrange(n, vmin, vmax):
    return (vmax-vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#for c, m, zl, zh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
xs = [1, 2]
ys = [1, 2]
zs = [1, 2]
ax.scatter3D(xs, ys, zs, c='black', alpha=1)

l3d = Line3D( xs, ys, zs )
ax.add_line( l3d )

xs2 = [0, 2]
l3d2 = Line3D( xs2, ys, zs, linewidth=2.0 )
ax.add_line( l3d2 )

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.savefig( 'test.svg', transparent=True )

#plt.show()

