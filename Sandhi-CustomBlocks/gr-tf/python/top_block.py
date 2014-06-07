#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Thu Jun  5 14:28:31 2014
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
from sbhs import plot_sink
import multiorder_tf
import wx

class top_block(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Top Block")

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 32000
		self.i = i = 1

		##################################################
		# Blocks
		##################################################
		_i_sizer = wx.BoxSizer(wx.VERTICAL)
		self._i_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_i_sizer,
			value=self.i,
			callback=self.set_i,
			label='i',
			converter=forms.float_converter(),
			proportion=0,
		)
		self._i_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_i_sizer,
			value=self.i,
			callback=self.set_i,
			minimum=0,
			maximum=100,
			num_steps=100,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_i_sizer)
		self.plot_sink_0 = plot_sink.plot_sink_f(
			self.GetWin(),
			title="Scope Plot",
			vlen=1,
			decim=1,
		)
		self.Add(self.plot_sink_0.win)
		self.multiorder_tf_0 = multiorder_tf.multiorder_tf()
		self.multiorder_tf_0.set_parameters(1, i, 2, 0, 0,1, 2, 2, 0,0, 1, 1)
		    
		self.gr_sig_source_x_0 = gr.sig_source_f(samp_rate, gr.GR_COS_WAVE, 1000, 1, 0)

		##################################################
		# Connections
		##################################################
		self.connect((self.gr_sig_source_x_0, 0), (self.multiorder_tf_0, 0))
		self.connect((self.multiorder_tf_0, 0), (self.plot_sink_0, 0))


	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.gr_sig_source_x_0.set_sampling_freq(self.samp_rate)

	def get_i(self):
		return self.i

	def set_i(self, i):
		self.i = i
		self._i_slider.set_value(self.i)
		self._i_text_box.set_value(self.i)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)

