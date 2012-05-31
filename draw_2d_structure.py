from drawer_2d_structure import drawer_2d_structure
from drawer_3d_structure import drawer_3d_structure

structure_str = "nodes(loadedNode(360.0, 0.0, 0.0, false, false, true, 1), loadedNode(720.0, 0.0, 0.0, false, false, true, 2), fixedNode(0.0, 0.0, 0.0), fixedNode(0.0, 360.0, 0.0), node(583.69, 293.35, 0, false, false, true), node(486.03, 290.09, 0, false, false, true)) bar(bar(bar(bar(207, 457, 7.43, 1), 1000, 6.77, 1), bar(1002, bar(733, 254, 3.75, 1), 5.60, 0), 9.11, 1), bar(bar(bar(387, 213, 8.77, 0), 384, 5.98, 1), bar(167, 551, 9.03, 1), 0.53, 1), 0.16, 0)"
d2 = drawer_2d_structure( structure_str )
#d3 = drawer_3d_structure( structure_str )

#d2.show( )
d2.save( "test2d.eps" )
#d3.show( )
#d3.save( "test3d.eps" )

d2 = drawer_2d_structure( structure_str )
d2.save( "test2d.eps" )

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

