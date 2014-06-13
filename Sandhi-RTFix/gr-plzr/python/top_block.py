#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Fri Jun 13 11:49:22 2014
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import plzr
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
		self.plzr_plzr_0 = plzr.plzr()
		self.plzr_plzr_0.set_parameters("[1+s   2+3*s+4*s^2        5; 0        1-s             s]","[1+3*s   5-s^3           s+1;1+s     1+s+s^2      3*s-1]")
		self.gr_null_source_0 = gr.null_source(gr.sizeof_float*1)
		self.gr_null_sink_0 = gr.null_sink(gr.sizeof_float*1)

		##################################################
		# Connections
		##################################################
		self.connect((self.gr_null_source_0, 0), (self.plzr_plzr_0, 0))
		self.connect((self.plzr_plzr_0, 0), (self.gr_null_sink_0, 0))


	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)

