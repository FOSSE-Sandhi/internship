#!/usr/bin/env python
from xml.dom import minidom
import xml.dom
import sys
import os

class Parser:
	def __init__(self,grc_file):
		self.xmldoc = minidom.parse(grc_file)
		self.directory = ""
		pathsplit = grc_file.split("/")
		for i in range(1,len(pathsplit)-1):
			self.directory += "/"+pathsplit[i]
		#print "Dir:", self.directory
			
	def process(self,grc_file,cmd_args):
		'''
		Main processing and manipulation of .grc file happens here.
		@param cmd_ags: Command line arguements passed - These are the 
		parameters that need to be updated in the .grc file.
		'''
		print "Building flow graph...",
		first_child = self.xmldoc.firstChild
		lst = first_child.getElementsByTagName("key")
		#print cmd_args
		keys = map(lambda x: x.split("=")[0], cmd_args)
                values = map(lambda x: x.split("=")[1], cmd_args)
		table = zip(keys, values)
		table = dict(table) #table now contains a bunch of key-value pairs
		#Now, remove parameters in lst that need not be modified
		lst = filter(lambda x: x.firstChild.data in table.keys(), lst)
		
		#Update values of parameters still present in lst
		for i in lst:
			parent_node = i.parentNode
			value_node = parent_node.getElementsByTagName("value")
			old_child = value_node[0].firstChild
			new_child = self.xmldoc.createTextNode(table[i.firstChild.data])
			value_node[0].replaceChild(new_child,old_child)

		dst_file = self.directory + "/testps.grc"
		#write updated xml to a new file
		fp = open(dst_file,"w")
		fp.write(self.xmldoc.toxml())
		fp.close()
		print "Done"
		print "Generating top block...",
		os.system("grcc "+dst_file+" -d "+self.directory)
		print "Done"

if __name__ == "__main__":
	parser = Parser(sys.argv[1])
	parser.process(sys.argv[1],sys.argv[2:])

 
