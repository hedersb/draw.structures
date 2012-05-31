import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Line3D
import matplotlib.pyplot as plt
import matplotlib.lines as lines
from math import sqrt
from structure import structure

class drawer_3d_structure:

	def __init__(self, string_representation):
		self.structure = structure( string_representation )
	
	def save( self, file_name ):
		self.draw( )
		plt.savefig( file_name, transparent=True )
		
	def draw( self ):
		self.figure = plt.figure( )
		self.axes = self.figure.add_subplot( 111, projection='3d', aspect='equal' )
		self.axes.set_xlabel('x')
		self.axes.set_ylabel('y')
		self.axes.set_zlabel('z')
		#draw nodes
		for node in self.structure.nodes:
			xs = [ node[ 0 ] ]
			ys = [ node[ 1 ] ]
			zs = [ node[ 2 ] ]
			self.axes.scatter( xs, ys, zs, c='black', alpha=1 )
		#draw bars
		for bar in self.structure.bars:
			xs = [ self.structure.nodes[ bar.begin ][ 0 ], self.structure.nodes[ bar.end ][ 0 ] ]
			ys = [ self.structure.nodes[ bar.begin ][ 1 ], self.structure.nodes[ bar.end ][ 1 ] ]
			zs = [ self.structure.nodes[ bar.begin ][ 2 ], self.structure.nodes[ bar.end ][ 2 ] ]
			line = Line3D( xs, ys, zs, linewidth = sqrt( bar.parameter ), color="black" )
			self.axes.add_line( line )
		
		#self.axes.plot( )
			
	def show( self ):
		self.draw( )
		plt.show( )


