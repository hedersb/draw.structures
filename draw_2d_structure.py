from drawer_2d_structure import drawer_2d_structure
from drawer_3d_structure import drawer_3d_structure

structure_str = "nodes(loadedNode(250.0, 250.0, 0.0, false, false, true, 1), loadedNode(500.0, 250.0, 0.0, false, false, true, 2), loadedNode(750.0, 250.0, 0.0, false, false, true, 3), loadedNode(1000.0, 250.0, 0.0, false, false, true, 4), loadedNode(1250.0, 250.0, 0.0, false, false, true, 5), fixedNode(0.0, 0.0, 0.0), fixedNode(0.0, 250.0, 0.0),  node(241, 252, 0, false, false, true),  node(2, 3, 0, false, false, true),  node(245, 1, 0, false, false, true),  node(65, 232, 0, false, false, true),  node(214, 0, 0, false, false, true)) bar(138, bar(44, bar(130, bar(bar(bar(148, 209, 11.5, 1), bar(21, 127, 4.18, 1), 5.74, 0), bar(bar(107, bar(bar(bar(94, 30, 3.13, 0), bar(143, bar(bar(29, bar(132, 132, 22, 0), 19.9, 0), 114, 26.5, 0), 22, 0), 1.62, 1), 7, 14.2, 0), 7.22, 1), bar(160, bar(100, bar(52, bar(bar(bar(bar(219, 252, 2.63, 0), bar(bar(146, bar(bar(241, 124, 22.9, 0), bar(bar(bar(126, 114, 15.5, 0), bar(201, 144, 4.97, 1), 30, 0), bar(bar(bar(132, 227, 22, 1), bar(bar(bar(bar(49, 80, 2.93, 1), bar(150, bar(201, bar(8, 79, 16, 1), 2.88, 1), 30, 1), 16.9, 1), bar(194, bar(78, bar(bar(bar(110, 158, 4.49, 1), 183, 4.22, 0), 154, 3.09, 1), 22, 0), 2.62, 1), 3.84, 0), 123, 15.5, 0), 22, 1), bar(188, bar(168, 244, 2.63, 0), 3.47, 0), 22, 1), 4.18, 1), 11.5, 1), 4.49, 0), bar(243, 46, 7.22, 0), 2.88, 0), 1.99, 0), 147, 2.88, 0), bar(250, 139, 26.5, 0), 3.87, 1), 22, 0), 3.13, 1), 18.8, 1), 3.87, 0), 30, 0), 26.5, 0), 2.62, 0), 2.88, 1)"
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

