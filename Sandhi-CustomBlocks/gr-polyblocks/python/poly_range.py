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

class poly_range(gr.sync_block):
    """
    docstring for block poly_range
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="poly_range",
            in_sig = None,
            out_sig = None )


    def set_parameters(self,poly,x_range,xlabel,ylabel):
	self.poly = poly
	self.x_range = x_range
	self.xlabel = xlabel
	self.ylabel = ylabel
	self.plot_poly()

    def plot_poly(self):
	from polyrange_sci import polyrange
	polyrange(self.poly,self.x_range,self.xlabel,self.ylabel)
    '''
    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        return len(output_items[0])
    '''
