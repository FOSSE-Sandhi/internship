#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Sat Jun  7 12:15:20 2014
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import scifile
import wx

class top_block(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Top Block")

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 32000

		##################################################
		# Blocks
		##################################################
		self.scifile_generic_0 = scifile.scifile()
		self.scifile_generic_0.set_parameters("~/Downloads/test.sci", 1)
		    
		self.gr_null_source_0 = gr.null_source(gr.sizeof_float*1)
		self.gr_null_sink_0 = gr.null_sink(gr.sizeof_float*1)

		##################################################
		# Connections
		##################################################
		self.connect((self.gr_null_source_0, 0), (self.scifile_generic_0, 0))
		self.connect((self.scifile_generic_0, 0), (self.gr_null_sink_0, 0))


	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)

