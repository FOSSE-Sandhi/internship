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

import gras
import numpy
import serial
import time
from sbhs import *
from scan_machines import *

class sbfan(gras.Block):
    
    def __init__(self):
        gras.Block.__init__(self,
            name="sbfan",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])
	#from scan_machines import *
	print "Scanning Machines"
	scan_machines()
	# SBHS init
	self.new_device = Sbhs()
	self.new_device.connect(1)
	self.new_device.connect_device(0)


    def set_parameters(self,window,fan_value):
	self.n = window
	self.fan = fan_value


    def isIntegralWin(self,input_item,window):
	
	if(len(input_item) % window):
		raise Exception(" Value of Window should be an integral value of length of input items")

        
    def work(self, input_items, output_items):
        
	for heat_items in input_items[0]:
		print "Heat Written", heat_items
		# Set heat as 0 for negative values of heat
		if heat_items < 0:
			self.new_device.setHeat(0)
		else: 
			self.new_device.setHeat(heat_items)

		time.sleep(0.5)
		self.new_device.setFan(self.fan)
	
		time.sleep(0.5)

		
	#For zero Temperatures
	if not self.new_device.getTemp():
		raise Exception(" Check SBHS conection try relogging it and run scan_machines.py")
	#get temperature

	output_items[0][:1] = self.new_device.getTemp()
	print "temperature:" ,output_items[0][:1] 
	

	self.consume(0,1) #consume from port 0
	self.produce(0,self.n)

        

