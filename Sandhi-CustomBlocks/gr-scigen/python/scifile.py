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

class scifile(gras.Block):
    """
    docstring for block scifile
    """
    def __init__(self):
        gras.Block.__init__(self,
            name="scifile",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])

    def set_parameters(self,path,window):
	self.n = window
	self.path = path
	print self.path

    def isIntegralWin(self, input_item, window):
                if (len(input_item) % window ):
                        raise Exception("Value of Window should be an integral value of length of input items")



    def work(self, input_items, output_items):

   		import sciscipy 
		
                out_eval_string = "exec('" + self.path + "', -1)"
                sciscipy.eval(out_eval_string)

