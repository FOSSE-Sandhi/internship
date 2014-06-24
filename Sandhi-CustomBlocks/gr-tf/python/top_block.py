#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Tue Jun 17 16:57:14 2014
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
from sbhs import plot_sink
import tf_csim
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
		self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
			self.GetWin(),
			title="Scope Plot",
			sample_rate=samp_rate,
			v_scale=0,
			v_offset=0,
			t_scale=0,
			ac_couple=False,
			xy_mode=False,
			num_inputs=1,
			trig_mode=gr.gr_TRIG_MODE_AUTO,
			y_axis_label="Counts",
		)
		self.Add(self.wxgui_scopesink2_0.win)
		self.plot_sink_0 = plot_sink.plot_sink_f(
			self.GetWin(),
			title="Scope Plot",
			vlen=1,
			decim=1,
		)
		self.Add(self.plot_sink_0.win)
		self.gr_vector_source_x_0 = gr.vector_source_f((0, 0, 0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1), False, 1)
		self.controls_tf_csim_0 = tf_csim.tf_csim()
		self.controls_tf_csim_0.set_parameters(1, 1, 2, "s^2/(s^2+2)", 1)
		    

		##################################################
		# Connections
		##################################################
		self.connect((self.controls_tf_csim_0, 0), (self.wxgui_scopesink2_0, 0))
		self.connect((self.controls_tf_csim_0, 0), (self.plot_sink_0, 0))
		self.connect((self.gr_vector_source_x_0, 0), (self.controls_tf_csim_0, 0))


	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)

