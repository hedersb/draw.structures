from drawer_2d_structure import drawer_2d_structure
from drawer_3d_structure import drawer_3d_structure

structure_str = "nodes(loadedNode(250.0, 250.0, 0.0, false, false, true, 1), loadedNode(500.0, 250.0, 0.0, false, false, true, 2), loadedNode(750.0, 250.0, 0.0, false, false, true, 3), loadedNode(1000.0, 250.0, 0.0, false, false, true, 4), loadedNode(1250.0, 250.0, 0.0, false, false, true, 5), fixedNode(0.0, 0.0, 0.0), fixedNode(0.0, 250.0, 0.0),  node(223, 6, 0, false, false, true), node(30, 147, 0, false, false, true), node(221, 9, 0, false, false, true),  node(90, 6, 0, false, false, true)) bar(bar(bar(bar(bar(bar(177, 179, 4.59, 1), bar(bar(bar(bar(246, bar(bar(147, 124, 1.62, 0), 147, 3.87, 1), 13.5, 0), bar(171, bar(bar(bar(bar(bar(bar(bar(bar(bar(bar(99, bar(118, 155, 2.13, 1), 4.97, 1), 74, 3.09, 0), bar(108, 140, 16, 0), 1.99, 0), 137, 33.5, 1), 162, 33.5, 0), bar(256, bar(bar(bar(77, bar(205, bar(bar(bar(bar(bar(bar(236, bar(bar(bar(bar(211, 70, 11.5, 1), 104, 4.18, 1), 113, 16, 0), bar(bar(bar(214, bar(189, bar(bar(138, bar(bar(256, 90, 7.97, 0), 13, 1.8, 1), 22.9, 0), 250, 26.5, 0), 30, 0), 33.5, 0), bar(155, bar(bar(22, bar(bar(bar(184, bar(bar(bar(19, bar(229, 86, 4.8, 1), 5.74, 0), bar(85, bar(3, bar(75, bar(41, bar(67, 212, 3.63, 0), 3.09, 0), 33.5, 1), 16.9, 1), 1.62, 0), 2.93, 0), bar(bar(133, 9, 7.97, 1), 21, 30, 1), 3.09, 0), 1.99, 1), bar(bar(122, 183, 19.9, 1), bar(157, bar(bar(123, 203, 3.55, 1), 37, 3.88, 1), 14.2, 1), 19.9, 1), 5.12, 0), bar(15, 60, 3.13, 1), 3.88, 0), 2.88, 0), 60, 11.5, 1), 3.38, 0), 3.87, 1), 52, 13.5, 0), 3.88, 0), 4.97, 0), bar(154, bar(bar(154, bar(bar(bar(bar(bar(208, bar(bar(bar(bar(bar(bar(255, 223, 4.22, 1), bar(bar(bar(64, bar(137, bar(128, bar(72, bar(166, 20, 3.47, 0), 3.38, 0), 3.88, 0), 13.5, 0), 3.55, 1), bar(156, 146, 3.88, 0), 26.5, 1), 102, 14.2, 1), 3.55, 1), 91, 4.49, 1), 49, 7.97, 0), bar(43, bar(207, bar(bar(bar(249, bar(159, bar(bar(215, 251, 2.63, 1), 225, 4.59, 1), 3.38, 0), 26.5, 1), 119, 16, 0), 174, 3.88, 0), 14.2, 1), 19.9, 1), 2.93, 0), bar(86, bar(bar(122, bar(bar(bar(156, bar(7, bar(bar(bar(bar(152, bar(bar(86, 179, 2.62, 0), bar(bar(bar(bar(156, 231, 3.88, 0), 133, 13.5, 1), bar(222, 28, 4.22, 0), 14.2, 0), bar(232, 41, 4.18, 1), 4.22, 1), 1.62, 1), 22, 0), 183, 4.18, 0), bar(159, 69, 19.9, 0), 4.8, 1), 254, 1.8, 1), 3.55, 0), 30, 1), 109, 3.13, 1), 30, 4.22, 0), 19.9, 1), 181, 4.18, 1), 16.9, 0), 16, 1), 30, 0), bar(227, bar(52, bar(bar(221, 231, 16, 0), 196, 4.97, 0), 2.38, 1), 2.88, 1), 13.9, 0), bar(bar(133, bar(bar(144, 63, 2.62, 0), 255, 2.88, 1), 2.63, 1), 167, 4.8, 0), 3.38, 0), bar(bar(37, 178, 30, 1), bar(230, 189, 4.97, 0), 3.47, 1), 18.8, 0), bar(bar(bar(bar(5, 55, 22, 1), 247, 3.47, 1), 103, 2.62, 0), bar(bar(58, bar(bar(bar(227, 41, 3.09, 1), 112, 5.74, 0), 43, 16, 1), 33.5, 1), bar(bar(bar(bar(bar(bar(90, 192, 3.63, 0), 111, 15.5, 1), bar(154, bar(175, bar(8, 234, 2.93, 0), 13.5, 1), 2.93, 0), 2.88, 0), bar(bar(bar(bar(bar(236, 20, 19.9, 1), 216, 19.9, 0), bar(22, 192, 22.9, 0), 5.74, 0), 50, 5.74, 0), bar(bar(164, bar(170, 190, 22, 0), 2.13, 0), bar(bar(33, bar(bar(153, 157, 14.2, 1), 191, 3.55, 0), 5.12, 1), 127, 16.9, 1), 5.12, 0), 4.18, 0), 2.63, 1), 151, 4.8, 1), 88, 2.63, 0), 13.9, 1), 5.12, 0), 14.2, 1), 3.87, 0), bar(bar(25, 56, 1.8, 1), 58, 3.88, 1), 3.84, 0), 3.84, 1), 13.5, 1), bar(180, 70, 4.59, 0), 14.2, 1), 40, 15.5, 0), 83, 11.5, 1), 28, 14.2, 1), 7.22, 0), 4.8, 0), 226, 3.13, 1), 232, 3.55, 0), 3.63, 1), 5.74, 0), bar(146, bar(50, 22, 3.88, 1), 18.8, 0), 1.62, 0), bar(184, 204, 14.2, 1), 30, 0), 58, 7.97, 1), 61, 13.9, 1), 3.55, 1), 18.8, 1), 40, 22, 1), 48, 16, 0), 4.8, 1), 243, 1.62, 0), bar(bar(110, 55, 3.63, 0), 87, 3.63, 0), 3.38, 1), 184, 5.74, 1), 84, 1.99, 1)"
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

