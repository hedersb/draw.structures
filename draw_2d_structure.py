from drawer_2d_structure import drawer_2d_structure
from drawer_3d_structure import drawer_3d_structure

structure_str = "nodes(loadedNode(360.0, 0.0, 0.0, false, false, true, 1), loadedNode(720.0, 0.0, 0.0, false, false, true, 2), fixedNode(0.0, 0.0, 0.0), fixedNode(0.0, 360.0, 0.0),   node(520, 271, 0, false, false, true)) bar(12, bar(bar(65, 104, 33.5, 0), bar(bar(162, bar(156, bar(158, bar(98, bar(37, bar(176, bar(bar(bar(256, 94, 11.5, 0), bar(150, 218, 26.5, 1), 3.87, 0), 168, 26.5, 1), 18.8, 0), 4.97, 1), 19.9, 1), 4.22, 1), 3.87, 1), 1.62, 0), 18, 7.22, 0), 16, 1), 1.62, 0)"
d2 = drawer_2d_structure( structure_str )
#d3 = drawer_3d_structure( structure_str )

#d2.show( )
d2.save( "test2d.eps" )
#d3.show( )
#d3.save( "test3d.eps" )

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

