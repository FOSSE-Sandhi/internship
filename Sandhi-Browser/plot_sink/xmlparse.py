#!/usr/bin/env python
from xml.dom import minidom
import xml.dom
import sys
import os

SRC_FILE_PATH = "/home/anoop/IITB/gr-howto2/python/howto2.grc"
DST_FILE_PATH = "/home/anoop/IITB/gr-howto2/python/testing.grc"
DST_FOLDER = "/home/anoop/IITB/gr-howto2/python"

class Parser:
	def __init__(self):
		self.xmldoc = minidom.parse(SRC_FILE_PATH)
	
	def process(self,cmd_args):
		'''
		Main processing and manipulation of .grc file happens here.
		@param cmd_ags: Command line arguements passed - These are the 
		parameters that need to be updated in the .grc file.
		'''
		first_child = self.xmldoc.firstChild
		lst = first_child.getElementsByTagName("key")
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

		#write updated xml to a new file
		fp = open(DST_FILE_PATH,"w")
		fp.write(self.xmldoc.toxml())
		fp.close()

		os.system("grcc "+DST_FILE_PATH+" -d "+DST_FOLDER)

if __name__ == "__main__":
	parser = Parser()
	parser.process(sys.argv[1:])

 
