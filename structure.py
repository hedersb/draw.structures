class truss_bar:
	begin = 1
	end = 2
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
			remaining = self.fillDataNodes( string_representation )
			self.fillDataBars( remaining )
	
	def fillDataNodes( self, string_representation ):
		string_representation.lstrip() 
		i_begin = string_representation.find("(")
		function_name = string_representation[ : i_begin ].strip()
		if function_name == "nodes":
			i_end = string_representation.find("bar")
			count = 1
			parameters = string_representation[ i_begin + 1 : i_end ]
			string_return = string_representation[ i_end : ]
			i_begin = parameters.find("(")
			while ( i_begin > 0 ):
				node = [ 0.0, 0.0, 0.0 ]
				function_name = parameters[ : i_begin ].strip()
				i_cota = function_name.find(",")
				if i_cota >= 0:
					function_name = function_name[ i_cota + 1 : ].lstrip()
				
				#TODO: the order of the nodes is fundamental -- better increase
				if function_name == "node" or function_name == "fixedNode" or function_name == "loadedNode":
					parameters = parameters[ i_begin + 1: ]
					i = 0
					while i < 2:
						i_cota = parameters.find( "," )
#						print parameters[ : i_cota ].strip( )
						node[ i ] = float( parameters[ : i_cota ].strip( ) )
						parameters = parameters[ i_cota + 1 : ]
						i += 1
					if function_name == "fixedNode":
						i_cota = parameters.find( ")" )
					else:
						i_cota = parameters.find( "," )
					node[ i ] = float( parameters[ : i_cota ].strip( ) )
#					print node
					self.nodes.append( node )
				else:
					print( "The function '" + function_name + "' is not recognized." )
					return ""
				
				parameters = parameters[  parameters.find(")") + 1 : ]
				i_begin = parameters.find("(")
			
			return string_return
		else:
			print( "The first function must be nodes." )
			return ""
		
	def fillDataBars( self, string_representation ):
		string_representation.lstrip() 
		i_begin = string_representation.find("(")
		if i_begin < 0:
#			print "STR rep: " + string_representation
			return int( string_representation ) % len(self.nodes)
		else:
			function_name = string_representation[ : i_begin ].strip()
			parameters = string_representation[ i_begin+1 : ]
			if function_name == "bar":
				bar = truss_bar( )
				count = 0
				i = 0
				while not (parameters[ i ] == "," and count == 0):
					if parameters[ i ] == "(":
						count += 1
					elif parameters[ i ] == ")":
						count -= 1
					i += 1
				bar.begin = self.fillDataBars( parameters[ : i ] )
#				print "BEGIN: " + str( bar.begin )
				parameters = parameters[ i + 1: ]
				i = 0
				while not (parameters[ i ] == "," and count == 0):
					if parameters[ i ] == "(":
						count += 1
					elif parameters[ i ] == ")":
						count -= 1
					i += 1
				bar.end = self.fillDataBars( parameters[ : i ] )
#				print "END: " + str( bar.end )
				parameters = parameters[ i + 1: ]
				i_comma = parameters.rfind( "," )
				bar.parameter = float( parameters[ : i_comma ].strip( ) )
#				print "PARAM: " + str( bar.parameter )
				self.bars.append( bar )
				parameters = parameters[ i_comma + 1: parameters.rfind( ")" ) ].lstrip( ).strip( )
				returnNode = int( parameters )
				if returnNode == 0:
#					print "RETURN: " + str( returnNode ) + " -- " + str( bar.begin )
					return bar.begin #return left side node
				else:
#					print "RETURN: " + str( returnNode ) + " -- " + str( bar.end )
					return bar.end   #return right side node
			else:
				print( "Unrecognized function: " + function_name )
		




