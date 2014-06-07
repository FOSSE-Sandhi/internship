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
from scifile import scifile
import numpy

class qa_scifile (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
       
                src0 = numpy.arange(0,3.1316,1)

                src0 = gr.vector_source_f(src0)

                sqr = scifile()
                sqr.set_parameters("test.sci",-1)

                dst = gr.vector_sink_f()

                self.tb.connect(src0,sqr)
                self.tb.connect(sqr,dst)
		
                self.tb.run()

                #result_data = dst.data()
                #print result_data, "Result data"




if __name__ == '__main__':
    gr_unittest.main()
