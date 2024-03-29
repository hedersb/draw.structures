import numpy as np
from mpl_toolkits.mplot3d import Axes3D
#from mpl_toolkits.mplot3d.art3d import Line3D
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib.lines as lines
from math import sqrt
from structure import structure

class drawer_2d_structure:

	def __init__(self, string_representation):
		self.structure = structure( string_representation )
	
	def save( self, file_name ):
		self.draw( )
		plt.savefig( file_name, transparent=True )
		
	def draw( self ):
		self.figure = plt.figure( )
		self.axes = self.figure.add_subplot( 111, aspect='equal' )
		self.axes.set_xlabel('x')
		self.axes.set_ylabel('y')
		#draw nodes
		for node in self.structure.nodes:
			xs = [ node[ 0 ] ]
			ys = [ node[ 1 ] ]
			self.axes.scatter( xs, ys, c='black', alpha=1 )
		#draw bars
		for bar in self.structure.bars:
			xs = [ self.structure.nodes[ bar.begin ][ 0 ], self.structure.nodes[ bar.end ][ 0 ] ]
			ys = [ self.structure.nodes[ bar.begin ][ 1 ], self.structure.nodes[ bar.end ][ 1 ] ]
			line = Line2D( xs, ys, linewidth = sqrt( bar.parameter ), color="black" )
			self.axes.add_line( line )
		
		self.axes.plot( )
			
	def show( self ):
		self.draw( )
		plt.show( )


