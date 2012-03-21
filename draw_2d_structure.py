from drawer_2d_structure import drawer_2d_structure
from drawer_3d_structure import drawer_3d_structure

structure_str = "bar( bar(node(0.0, 0.0, 0.0, true, true, true), bar(node(0.0, 250.0, 0.0, true, true, true), bar(loadedNode(250.0, 250.0, 0.0, false, false, true, 1), bar(loadedNode(500.0, 250.0, 0.0, false, false, true, 2), bar(loadedNode(750.0, 250.0, 0.0, false, false, true, 3), bar(loadedNode(1000.0, 250.0, 0.0, false, false, true, 4), loadedNode(1250.0, 250.0, 0.0, false, false, true, 5), 3.55), 2.63), 4.18), 15.5), 4.22), 1.62), bar(bar(bar(bar(bar(node(303.19, 7.86, 0.0, false, false, true), bar(bar(loadedNode(1000.0, 250.0, 0.0, false, false, true, 4), loadedNode(500.0, 250.0, 0.0, false, false, true, 2), 1.62), loadedNode(500.0, 250.0, 0.0, false, false, true, 2), 1.8), 2.63), loadedNode(750.0, 250.0, 0.0, false, false, true, 3), 1.8), node(9.34, 5.60, 0.0, false, false, true), 3.63), loadedNode(1250.0, 250.0, 0.0, false, false, true, 5), 4.22), bar(bar(bar(bar(bar(node(0.0, 250.0, 0.0, true, true, true), node(0.0, 250.0, 0.0, true, true, true), 3.09), bar(bar(node(0.0, 0.0, 0.0, true, true, true), bar(node(0.0, 0.0, 0.0, true, true, true), loadedNode(250.0, 250.0, 0.0, false, false, true, 1), 1.62), 2.93), loadedNode(500.0, 250.0, 0.0, false, false, true, 2), 16), 2.13), loadedNode(500.0, 250.0, 0.0, false, false, true, 2), 3.87), node(0.0, 250.0, 0.0, true, true, true), 1.8), loadedNode(250.0, 250.0, 0.0, false, false, true, 1), 3.13), 3.47), 18.8)"
d2 = drawer_2d_structure( structure_str )
d3 = drawer_3d_structure( structure_str )

#d2.show( )
d2.save( "test2d.eps" )
#d3.show( )
d3.save( "test3d.eps" )

#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')

#xs = [1, 2]
#ys = [1, 2]
#zs = [1, 2]
#ax.scatter3D(xs, ys, zs, c='black', alpha=1)

#l3d = Line3D( xs, ys, zs )
#ax.add_line( l3d )

#xs2 = [0, 2]
#l3d2 = Line3D( xs2, ys, zs, linewidth=2.0 )
#ax.add_line( l3d2 )

#ax.set_xlabel('x')
#ax.set_ylabel('y')
#ax.set_zlabel('z')

#plt.savefig( 'test.svg', transparent=True )

#plt.show()

