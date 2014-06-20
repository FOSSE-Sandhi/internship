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
from power import power

class qa_power (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        # set up fg
	src_data1 = (2,3,4,1,4)
	src_data2 = (3,3,2,4,-1)
	expected_data = (8,27,16,1,0.25)
	src1 = gr.vector_source_f(src_data1)
	src2 = gr.vector_source_f(src_data2)
	sqr = power()
	dst = gr.vector_sink_f()
	self.tb.connect(src1,(sqr,0))
	self.tb.connect(src2,(sqr,1))
	self.tb.connect(sqr,dst)
	self.tb.run ()
	result_data = dst.data()
	print result_data
	self.assertFloatTuplesAlmostEqual(result_data,expected_data,6)
        # check data


if __name__ == '__main__':
    gr_unittest.main()
