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

from gnuradio import gr, gr_unittest
from poly_range import poly_range
import numpy

class qa_poly_range (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        # set up fg
        src0 = gr.vector_source_f(numpy.arange(0,3.1415,0.01))
	sqr = poly_range()
	sqr.set_parameters("10 -2*x + 15*x^2 + x^3","-40:0.01:40","x","y")

	dst = gr.vector_sink_f()
	self.tb.connect(src0,sqr)
	self.tb.connect(sqr,dst)
	self.tb.run ()
        # check data


if __name__ == '__main__':
    gr_unittest.main()
