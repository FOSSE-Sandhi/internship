#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Tue Jun 10 15:27:52 2014
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
from sbhs import plot_sink
import gnuradio.sbhs.gr_controller as gr_controller
import gnuradio.sbhs.sbfan as sbfan
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
		_f_sizer = wx.BoxSizer(wx.VERTICAL)
                self._f_text_box = forms.text_box(
                        parent=self.GetWin(),
                        sizer=_f_sizer,
                        value=self.f,
                        callback=self.set_f,
                        label="f",
                        converter=forms.float_converter(),
                        proportion=0,
                )
                self._f_slider = forms.slider(
                        parent=self.GetWin(),
                        sizer=_f_sizer,
                        value=self.f,
                        callback=self.set_f,
                        minimum=10,
                        maximum=80,
			num_steps=100,
                        style=wx.SL_HORIZONTAL,
                        cast=float,
                        proportion=1,
                )
                self.Add(_f_sizer)
                self.scigen_generic_0 = scigen.generic()
                self.scigen_generic_0.set_parameters("sin", 1)

                self.plot_sink_0 = plot_sink.plot_sink_f(
                        self.GetWin(),
                        title="Scope Plot",
                        vlen=1,
                        decim=1,
                )
                self.Add(self.plot_sink_0.win)
                self.gr_sig_source_x_0 = gr.sig_source_f(samp_rate, gr.GR_COS_WAVE, 10, f, 0)
		
	
		self.sbhs_controller_0 = gr_controller.sbhs_controller()
		self.sbhs_controller_0.set_parameters(1, 1, 1, 1, 1, 1)
		    
		self.sbfan_0 = sbfan.sbfan()
		self.sbfan_0.set_parameters(1,40)
		    
		self.plot_sink_0 = plot_sink.plot_sink_f(
			self.GetWin(),
			title="Scope Plot",
			vlen=1,
			decim=1,
		)
		self.Add(self.plot_sink_0.win)
		self.const_source_x_0 = gr.sig_source_f(0, gr.GR_CONST_WAVE, 0, 0, 30)

		##################################################
		# Connections
		##################################################
		self.connect((self.const_source_x_0, 0), (self.sbhs_controller_0, 0))
		self.connect((self.sbhs_controller_0, 0), (self.sbfan_0, 0))
		self.connect((self.sbfan_0, 0), (self.plot_sink_0, 0))


	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)

