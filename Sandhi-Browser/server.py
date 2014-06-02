import urllib
import serial
import json
import re
import sbhs

class Server:
	def __init__(self):
		self.url = "http://localhost:8080/sign"
		self.heat = 0
		self.fan = 0
		self.temp = 0
		self.sbhs = sbhs.Sbhs()
		fp = open("map_machine_ids.txt","r")
                line = fp.read()
                line = line.strip()
                self.machine_id = line.split("=")[0]
                fp.close()

	def get_values(self):
		'''Retrieve posted values from URL'''
		url_obj = urllib.urlopen(self.url)
		url_data = url_obj.read()
		url_data = json.loads(url_data)
		self.heat = url_data[0]
		self.fan = url_data[1]
		print "heat:",self.heat,type(self.heat)
		print "fan:",self.fan,type(self.fan)
	
	def connect(self):
		'''Connect to device using machine id.'''
                try:
                        self.sbhs.connect(self.machine_id)
                except:
                        print "Could not connect to device."

        def setHeat(self):
		'''Set heat value for device.'''
                try:
                        self.sbhs.setHeat(self.heat)
                except:
                        print "Unable to set heat."

        def setFan(self):
		'''Set fan value for device.'''
                try:
                        self.sbhs.setFan(self.fan)
                except:
                        print "Unable to set fan."

        def getTemp(self):
		'''Get temperature from device.'''
                self.temp = self.sbhs.getTemp()
		return self.temp

        def disconnect(self):
		'''Disconnect device.'''
                self.sbhs.disconnect()

if __name__ == "__main__":
	server = Server()
	server.get_values()
	server.connect()
	server.setHeat()
	server.setFan()
	temps = []
	for i in range(100):
		#a = server.getTemp()
		a = i
		#print "Temp:",a
		temps.append(a)
	vals = urllib.urlencode({"temps":temps})
	url = urllib.urlopen("http://localhost:8080/response",vals)
	server.disconnect()	
