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

import wx
import numpy
from gnuradio import gr
import sciscipy
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

class bode(gr.sync_block):
    """
    magnitude and phase of the frequency
    response of a given transfer function
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="bode",
            in_sig=[numpy.float32],
            out_sig=[numpy.float])

    def set_parameters(self,a,b):
	self.a=a
	self.b=b
	self.nplot()

    def nplot(self):
	inp = "s=poly(0,'s');h=syslin('c',("+self.a+")/("+self.b+"));clf();bode(h,0.1,100)"
	sciscipy.eval(inp)

    def work(self, input_items, output_items):
        #Leave this unimplemented
	return len(output_items[0])
