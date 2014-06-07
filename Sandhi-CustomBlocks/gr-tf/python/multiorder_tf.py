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
import sciscipy

class multiorder_tf(gras.Block):
    """
    docstring for block multiorder_tf
    """
    def __init__(self):
        gras.Block.__init__(self,
            name="multiorder_tf",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])

    def set_parameters(self,P,I,D,n0,n1,n2,n3,d0,d1,d2,d3,f):
	self.param0 = P
	self.param1 = I
	self.param2 = D
	self.param3 = n0
	self.param4 = n1
	self.param5 = n2
	self.param6 = n3
	self.param7 = d0
	self.param8 = d1
	self.param9 = d2
	self.param10 = d3
	self.n = f	#window

    def isIntegralWin(self, input_item, window):
	if (len(input_item) % window):
		raise Exception("Value of Window should be an integral value of length of input items")


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
	from multiorder_tf_sci import csim	

        out[:self.n] = csim(self.param0,self.param1,self.param2,self.param3,self.param4,self.param5,self.param6,self.param7,self.param8,self.param9,self.param10,in0[:self.n].tolist()) 
        
	print "OUT", out[:self.n]
	
	self.consume(0,self.n)
	self.produce(0,self.n)

