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
    docstring for block bode
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="bode",
            in_sig=[numpy.float32],
            out_sig=[numpy.float])

    def set_parameters(self,a,b,c,d):
	self.a=a
	self.b=b
#	self.c=c
#	self.d=d
	self.nplot()

    def nplot(self):
	a1,a2,a3,a4=self.a.split(',')
	b1,b2,b3,b4=self.b.split(',')
#	c1,c2,c3,c4=self.c.split(',')	
#	d1,d2,d3,d4=self.d.split(',')
#	inp = "s=poly(0,'s');h=syslin('c',("+str(a1)+"*s^3+"+str(a2)+"*s^2+"+str(a3)+"*s+"+str(a4)+")/("+str(b1)+"*s^3+"+str(b2)+"*s^2+"+str(b3)+"*s+"+str(b4)+"));h1=h*syslin('c',("+str(c1)+"*s^3+"+str(c2)+"*s^2+"+str(c3)+"*s+"+str(c4)+")/("+str(d1)+"*s^3+"+str(d2)+"*s^2+"+str(d3)+"*s+"+str(d4)+"));clf();    bode(h,0.1,100)"
	inp = "s=poly(0,'s');h=syslin('c',("+str(a1)+"*s^3+"+str(a2)+"*s^2+"+str(a3)+"*s+"+str(a4)+")/("+str(b1)+"*s^3+"+str(b2)+"*s^2+"+str(b3)+"*s+"+str(b4)+"));clf();bode(h,0.1,100)"
	sciscipy.eval(inp)

    def work(self, input_items, output_items):
	"""
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
        out[:] = in0
	"""
        return len(output_items[0])
