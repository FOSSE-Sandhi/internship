#/usr/bin/env python
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
class power(gras.Block):
    """
    docstring for block power
    """
    def __init__(self):
        gras.Block.__init__(self,
            name="power",
            in_sig=[numpy.float32,numpy.float32],
            out_sig=[numpy.float32])


    def work(self, input_items, output_items):
        
	in0 = input_items[0]
	in1 = input_items[1]
        out = output_items[0]
        # <+signal processing here+>
        out[:1] = pow(in0[:1],in1[:1])
	self.consume(0,1)
	self.consume(1,1)
	self.produce(0,1)
        #return len(output_items[0])

