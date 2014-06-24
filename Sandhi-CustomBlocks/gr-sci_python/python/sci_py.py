#!/usr/bin/env python
# 
# Copyright 2014 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr
import gras
import time
class sci_py(gras.Block):
    """
    docstring for block sci_py
    """
    def __init__(self):
        gras.Block.__init__(self,
            name="sci_py",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])

	self.ret_array = []
    def set_parameters(self,path,window):
	self.path = path
	self.n = window
	import sciscipy
	f = open(self.path)
	x = f.read()
	x = x.split("\n")
	code_string = ""
	
	for i in range(0,len(x)):
		code_string += x[i]

	sciscipy.eval(code_string)
	self.ret_array = sciscipy.read("y")
	#print self.ret_array


    def work(self, input_items, output_items):
        #in0 = input_items[0]
        out = output_items[0]
	self.ret_array = numpy.array(self.ret_array)
        # <+signal processing here+>
        output_items[0][:len(self.ret_array)] = self.ret_array.tolist()
	self.produce(0,len(self.ret_array))	
	self.consume(0,1)
	'''
	for i in range(self.n):
		print output_items[0][i]
		self.produce(0,1)
	'''
        #return len(output_items[0])
