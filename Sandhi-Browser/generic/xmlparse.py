#!/usr/bin/env python
from xml.dom import minidom
import xml.dom
import sys
import os

#SRC_FILE_PATH = "/home/anoop/IITB/gr-howto2/python/howto2_fs.grc"
#DST_FILE_PATH = "/home/anoop/IITB/gr-howto2/python/test_fs.grc"
#DST_FOLDER = "/home/anoop/IITB/gr-howto2/python"

DIR_PATH = "/home/anoop/IITB/gr-howto2/python"

class Parser:
	def __init__(self,sink):
		if sink == "file sink":		
			self.xmldoc = minidom.parse(DIR_PATH + "/howto2_fs.grc")
		elif sink == "plot sink":
			self.xmldoc = minidom.parse(DIR_PATH + "/howto2.grc")
	
	def process(self,sink,cmd_args):
		'''
		Main processing and manipulation of .grc file happens here.
		@param cmd_ags: Command line arguements passed - These are the 
		parameters that need to be updated in the .grc file.
		'''
		print "Building flow graph...",
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
		if sink == "file sink":
			dst_file = DIR_PATH + "/test_fs.grc"
		elif sink == "plot sink":
			dst_file = DIR_PATH + "/test_ps.grc"
		
		fp = open(dst_file,"w")
		fp.write(self.xmldoc.toxml())
		fp.close()
		print "Done"
		print "Generating top block...",
		os.system("grcc "+dst_file+" -d "+DIR_PATH)
		print "Done"

if __name__ == "__main__":
	parser = Parser(sys.argv[1])
	parser.process(sys.argv[1],sys.argv[2:])

 
