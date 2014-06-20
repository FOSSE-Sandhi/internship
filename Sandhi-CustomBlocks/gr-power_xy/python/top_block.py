#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Thu Jun 19 11:32:55 2014
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import numbersink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import power
import wx

class top_block(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Top Block")

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 32000
		self.f = f = 2

		##################################################
		# Blocks
		##################################################
		_f_sizer = wx.BoxSizer(wx.VERTICAL)
		self._f_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_f_sizer,
			value=self.f,
			callback=self.set_f,
			label='f',
			converter=forms.int_converter(),
			proportion=0,
		)
		self._f_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_f_sizer,
			value=self.f,
			callback=self.set_f,
			minimum=0,
			maximum=100,
			num_steps=100,
			style=wx.SL_HORIZONTAL,
			cast=int,
			proportion=1,
		)
		self.Add(_f_sizer)
		self.wxgui_numbersink2_0 = numbersink2.number_sink_f(
			self.GetWin(),
			unit="Units",
			minval=-100,
			maxval=100,
			factor=1.0,
			decimal_places=10,
			ref_level=0,
			sample_rate=samp_rate,
			number_rate=15,
			average=False,
			avg_alpha=None,
			label="Number Plot",
			peak_hold=False,
			show_gauge=True,
		)
		self.Add(self.wxgui_numbersink2_0.win)
		self.power_xy_power_0_0 = power.power()
		self.power_xy_power_0 = power.power()
		self.const_source_x_0_0_0 = gr.sig_source_f(0, gr.GR_CONST_WAVE, 0, 0, 0.5)
		self.const_source_x_0_0 = gr.sig_source_f(0, gr.GR_CONST_WAVE, 0, 0, 2 + f)
		self.const_source_x_0 = gr.sig_source_f(0, gr.GR_CONST_WAVE, 0, 0, 23)

		##################################################
		# Connections
		##################################################
		self.connect((self.const_source_x_0_0, 0), (self.power_xy_power_0, 1))
		self.connect((self.const_source_x_0, 0), (self.power_xy_power_0, 0))
		self.connect((self.power_xy_power_0, 0), (self.power_xy_power_0_0, 0))
		self.connect((self.const_source_x_0_0_0, 0), (self.power_xy_power_0_0, 1))
		self.connect((self.power_xy_power_0_0, 0), (self.wxgui_numbersink2_0, 0))


	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate

	def get_f(self):
		return self.f

	def set_f(self, f):
		self.f = f
		self.const_source_x_0_0.set_offset(2 + self.f)
		self._f_slider.set_value(self.f)
		self._f_text_box.set_value(self.f)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)

