from drawer_2d_structure import drawer_2d_structure
from drawer_3d_structure import drawer_3d_structure

structure_str = "bar( bar( node(0.0, 0.0, 0.0, true, true, true), bar( node(0.0, 250.0, 0.0, true, true, true), bar( loadedNode(250.0, 250.0, 0.0, false, false, true, 1), bar( loadedNode(500.0, 250.0, 0.0, false, false, true, 2), bar( loadedNode(750.0, 250.0, 0.0, false, false, true, 3), bar( loadedNode(1000.0, 250.0, 0.0, false, false, true, 4), loadedNode(1250.0, 250.0, 0.0, false, false, true, 5), 30), 33.5), 33.5), 30), 33.5), 2.93), bar( bar( bar( bar( node(333, 123, 0.0, false, false, true), loadedNode(250.0, 250.0, 0.0, false, false, true, 1), 16.9), loadedNode(750.0, 250.0, 0.0, false, false, true, 3), 33.5), bar( bar( bar( bar( bar( bar( node(528, 7, 0.0, false, false, true), loadedNode(1000.0, 250.0, 0.0, false, false, true, 4), 30), node(0.0, 0.0, 0.0, true, true, true), 26.5), loadedNode(1250.0, 250.0, 0.0, false, false, true, 5), 33.5), node(0.0, 0.0, 0.0, true, true, true), 30), loadedNode(500.0, 250.0, 0.0, false, false, true, 2), 16.9), node(0.0, 250.0, 0.0, true, true, true), 30), 2.62), loadedNode(1250.0, 250.0, 0.0, false, false, true, 5), 33.5), 33.5)"
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

