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
	numberOfRequiredNodes = 0
	def __init__(self, string_representation):
		if ( string_representation != "" ):
			remaining = self.fillDataNodes( string_representation )
			self.fillDataBars( remaining )
#			print( self.nodes )
#			print( self.bars )
			nNodes = len( self.nodes )
			nBars = len( self.bars )
			self.fixStructure( )
			while nNodes != len( self.nodes ) or nBars != len( self.bars ):
#				print( "\nwhile\n" )
#				print( self.nodes )
#				print( self.bars )
				nNodes = len( self.nodes )
				nBars = len( self.bars )
				self.fixStructure( )
	
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
				if function_name == "fixedNode" or function_name == "loadedNode":
					self.numberOfRequiredNodes += 1;
					
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
					# if there is an equal node then this one is not included
#					include = True
#					i = 0
#					while include and i < len( self.nodes ):
#						include = not ( self.nodes[ i ][ 0 ] == node[ 0 ] and self.nodes[ i ][ 1 ] == node[ 1 ] and self.nodes[ i ][ 2 ] == node[ 2 ] )
#						i += 1
#					#
#					if include:
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
			#assuming that string_representation is in [1; 256]
			#return a value between 0 and the number of nodes
			return (int( string_representation ) - 1) % len(self.nodes)
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
				
				#if there is an equal bar, it is used the lightest one
#				include = True
#				i = 0
#				while include and i < len( self.bars ):
#					include = not ( self.bars[ i ].begin == bar.begin and self.bars[ i ].end == bar.end )
#					i += 1
#				#
#				if include:
				self.bars.append( bar )
#				elif bar.parameter < self.bars[ i-1 ].parameter:
#					self.bars[ i-1 ].parameter = bar.parameter
					
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
		
	def fixStructure( self ):
		i = self.numberOfRequiredNodes
		while ( i < len( self.nodes ) ):
			flagNode = -1
			j = 0
			while j < self.numberOfRequiredNodes and flagNode == -1:
				if 	self.nodes[ i ][ 0 ] == self.nodes[ j ][ 0 ] and self.nodes[ i ][ 1 ] == self.nodes[ j ][ 1 ] and self.nodes[ i ][ 2 ] == self.nodes[ j ][ 2 ]:
					flagNode = j
				j += 1
			if flagNode == -1:
				j = i + 1
				while j < len( self.nodes ) and flagNode == -1:
					if 	self.nodes[ i ][ 0 ] == self.nodes[ j ][ 0 ] and self.nodes[ i ][ 1 ] == self.nodes[ j ][ 1 ] and self.nodes[ i ][ 2 ] == self.nodes[ j ][ 2 ]:
						flagNode = j
					j += 1
			
			if flagNode != -1:
				self.nodes[ i ][ 0 ] = -1
				flagNode += 1
				k = 0
				for bar in self.bars:
					if bar.begin == i:
						bar.begin = flagNode
					if bar.end == i:
						bar.end = flagNode
			else:
				flagNode = 0
				for bar in self.bars:
					if bar.begin == i:
						flagNode += 1
					if bar.end == i:
						flagNode += 1
				if flagNode < 2:
					self.nodes[ i ][ 0 ] = -1
					for bar in self.bars:
						if bar.begin == i:
							bar.begin = -1
						if bar.end == i:
							bar.end = -1
			#end-else
			if self.nodes[ i ][ 0 ] == -1:
			
				#remove node -- equivalent to the replacement of the c++ code
				for bar in self.bars:
					if bar.begin > i:
						bar.begin -= 1
					if bar.end > i:
						bar.end -= 1
				del self.nodes[ i ]
				i -= 1
			
			i += 1
		#end-while-nodes
		i = 0
		while i < len( self.bars ):
			if self.bars[ i ].begin == self.bars[ i ].end or self.bars[ i ].begin == -1 or self.bars[ i ].end == -1:
				flagBar = -2
			else:
				flagBar = -1
			j = i + 1
			while j < len( self.bars ) and flagBar == -1:
				if (self.bars[ i ].begin == self.bars[ j ].begin and self.bars[ i ].end == self.bars[ j ].end ) or (self.bars[ i ].begin == self.bars[ j ].end and self.bars[ i ].end == self.bars[ j ].begin ):
					flagBar = j
				j += 1
			if flagBar != -1:
				if flagBar > -1:
					if self.bars[ i ].parameter < self.bars[ flagBar ].parameter:
						self.bars[ flagBar ].parameter = self.bars[ i ].parameter;
				#remove bar -- equivalent to the replacement of the c++ code
				del self.bars[ i ]
				i -= 1
			i += 1
		#end-while-bars
			



