from drawer_2d_structure import drawer_2d_structure
import sys

folder = sys.argv[ 1 ]
imageNumber = sys.argv[ 2 ] # formated
line = sys.argv[ 3 ]

#print line
#print imageNumber

if line.find( "Iteration: " ) == 0:
	record = line.split( "|", 7 )
	objFunctionEvaluations = record[ 1 ].split( ": " )[ 1 ].rstrip( )
	structureStr = record[ 6 ].split( ": " )[ 1 ].rstrip( )
	#print( objFunctionEvaluations + "\t" + structureStr )
	
	structure2d = drawer_2d_structure( structureStr )
	structure2d.save( folder + "/structure2d_" + imageNumber + ".png" )
	print( "Image created (" + objFunctionEvaluations + "): " + folder + "/structure2d_" + imageNumber + ".png" )
	


