class truss_bar:
	begin = ( 0.0, 0.0, 0.0)
	end = ( 0.0, 0.0, 0.0 )
	parameter = 0.0
	
	def __init__(self):
		self.parameter = 0.0
	
	def __str__(self):
		return "Bar( " + str(self.begin) + "; " + str(self.end) + "; " + str(self.parameter) + ")"
	
	def __repr__(self):
		return self.__str__( )
		

class structure:
	nodes = []
	bars = []
	def __init__(self, string_representation):
		if ( string_representation != "" ):
			self.fillData( string_representation )
		
	def fillData( self, string_representation ):
		string_representation.lstrip()
		i_begin = string_representation.find("(")
		function_name = string_representation[ : i_begin ].strip()
		parameters = string_representation[ i_begin + 1 : ]
		if function_name == "bar":
			count = 0
			i = 0
			while not (parameters[ i ] == "," and count == 0):
				if parameters[ i ] == "(":
					count += 1
				elif parameters[ i ] == ")":
					count -= 1
				i += 1
			bar = truss_bar( )
			bar.begin = self.fillData( parameters[ : i ] )
			parameters = parameters[ i + 1: ]
			i = 0
			while not (parameters[ i ] == "," and count == 0):
				if parameters[ i ] == "(":
					count += 1
				elif parameters[ i ] == ")":
					count -= 1
				i += 1
			bar.end = self.fillData( parameters[ : i ] )
			parameters = parameters[ i + 1: parameters.rfind( ")" ) ]
			bar.parameter = float( parameters.strip( ) )
			self.bars.append( bar )
#			return bar.begin #return left side node
			return bar.end   #return right side node
		elif function_name == "node" or function_name == "loadedNode":
			node = [ 0.0, 0.0, 0.0 ]
			i = 0
			while i < 3:
				iComma = parameters.find( "," )
				node[ i ] = float( parameters[ : iComma ].strip( ) )
				parameters = parameters[ iComma + 1 : ]
				i += 1
			self.nodes.append( node )
			return node
		else:
			print( "Unrecognized function: " + function_name )
		




