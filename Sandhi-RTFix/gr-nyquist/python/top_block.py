#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Fri Jun 13 11:50:23 2014
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import nyquist
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
		self.nyquist_block_nyquist_0 = nyquist.nyquist()
		self.nyquist_block_nyquist_0.set_parameters("0,1,2*0.9*10,100","0,1,2*0.3*10.1,102.01","0,1,2*0.1*15.1,228.01","0,1,2*0.9*15,225")
		self.gr_null_source_0 = gr.null_source(gr.sizeof_float*1)
		self.gr_null_sink_0 = gr.null_sink(gr.sizeof_float*1)

		##################################################
		# Connections
		##################################################
		self.connect((self.gr_null_source_0, 0), (self.nyquist_block_nyquist_0, 0))
		self.connect((self.nyquist_block_nyquist_0, 0), (self.gr_null_sink_0, 0))


	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)

