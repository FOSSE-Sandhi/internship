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


class tf_csim(gras.Block):
    """
    docstring for block tf_csim
    """
    def __init__(self):
        gras.Block.__init__(self,
            name="tf_csim",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])

    def set_parameters(self,p,i,d,n0,n1,d0,d1,f):
	self.param1 = p
	self.param2 = i
	self.param3 = d
	self.param4 = n0
	self.param5 = n1
	self.param6 = d0
	self.param7 = d1
	self.n = f #Window

    def isIntegralWin(self, input_item, window):
	if (len(input_item) % window):
		raise Exception("Value of Window should be an integral value of length of input items")


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
	from tf_csim_sci import csim

	if self.param1 == 0 and self.param2 == 0 and self.param3 == 0 and self.param4 ==0 and self.param5 == 0 and self.param6 == 0 and self.param7 == 0:
		out[:self.n] = in0[:self.n]
	else:	
	       	out[:self.n] = csim(self.param1, self.param2, self.param3, self.param4, self.param5, self.param6, self.param7, in0[:self.n].tolist())
        
	print "OUT", out[:self.n]

	self.consume(0,self.n)
	self.produce(0,self.n)

