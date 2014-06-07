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
from multiorder_tf import multiorder_tf

class qa_multiorder_tf (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        # set up fg
	src_data1 = [0]*100
        src_data2 = [1]*1000
        src_data = tuple(src_data1 + src_data2)

        src = gr.vector_source_f (src_data)
        sqr = multiorder_tf()
        sqr.set_parameters(1,0,0,0.5,1,0,1,0,1,0,0,1,1,0,1,1,1100)

        #Preload
        sqr.input_config(1).preload_items = 1
        dst = gr.vector_sink_f ()

        self.tb.connect(src,sqr)
        self.tb.connect(sqr,dst)

        self.tb.run ()
        # check data
        result_data = dst.data()

        import matplotlib.pyplot as plt
        plt.plot(result_data)
        plt.show()




if __name__ == '__main__':
    gr_unittest.main()
