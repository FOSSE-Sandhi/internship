#!/usr/bin/env python
import gviz_api
import threading
import urllib
import time
import json
import sbhs

#Number of iterations for the loop - to get a stable temperature value
NUM_ITER = 50 

sem = threading.Semaphore(1)

class Server:
	def __init__(self):
		self.heat = 0
		self.fan = 0
		self.temp = 0
		self.sbhs = sbhs.Sbhs()
		fp = open("map_machine_ids.txt","r")
                line = fp.read()
                line = line.strip()
                self.machine_id = line.split("=")[0]
                fp.close()

	def get_values(self,url_data):
		'''Retrieve posted values from URL'''
		url_data = json.loads(url_data)
		self.heat = url_data[0]
		self.fan = url_data[1]
		#print "heat:",self.heat,type(self.heat)
		#print "fan:",self.fan,type(self.fan)
	
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


def func(url_data):
	sem.acquire()
	server = Server()
	#print url_data,type(url_data)
	server.get_values(url_data)
	server.connect()
	server.setHeat()
	server.setFan()
	num_iter = NUM_ITER
	#temps = []
	tim = 0
	description = [('Time','string'),('Temperature','number')]
	table = gviz_api.DataTable(description)
        for i in range(NUM_ITER):
	        temperature = server.getTemp()
                #temperature = i
                #print "Temp:",a
                #temps.append([str(j),a])
		#j += 2
                #time.sleep(2)
       		#vals = urllib.urlencode({"temps":json.dumps(temps)})
		#print temps
		#temps.insert(0,["Time","Temperature"])
		#temps = json.dumps(temps)
		res = """
		<html>
 	 		<head>
    				<script type="text/javascript" src="https://www.google.com/jsapi"></script>
    				<script type="text/javascript">
      					var t;
					function redirect()
      					{		
						location.reload(true)
      					}
					if(%(i)d < (%(num_iter)d-1))
					{
						//refresh every 2 seconds
      						t = setTimeout("redirect();",2000)
					}
       					google.load("visualization", "1", {packages:["corechart"]});
      					google.setOnLoadCallback(drawChart);
      					function drawChart()
					{
						var data = new google.visualization.DataTable(%(values)s,0.6);
        					var options = {
          						title: 'Temperature vs Time'
        						};

        					var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
        					chart.draw(data, options);
      					}
    				</script>
  			</head>
  			<body>
    				<div id="chart_div" style="width: 1200px; height: 700px;"></div>
  			</body>
		</html>
"""

		
		table.AppendData([[str(tim),temperature]])
		values = table.ToJSon(columns_order=("Time","Temperature"))


	# Putting the JS code and JSon string into the template
		value = res % vars()

		vals = urllib.urlencode({"temps":value})
        	response_url = urllib.urlopen("http://localhost:8080/response",vals)
		time.sleep(2)
		tim += 2
        server.disconnect()
	sem.release()

	
class Threads(threading.Thread):
	def __init__(self,fn,url_data):
		threading.Thread.__init__(self,target=fn,args=url_data)
	def run(self):
		threading.Thread.run(self)

if __name__=="__main__":
	url = "http://localhost:8080/sign"
        request = False
        url_obj = None
        url_data = None
        prev_data = ""
	while(True):
		url_data = ""
                while(not request):
                        print "waiting for request"
                        try:
                                url_obj = urllib.urlopen(url)
                                url_data = url_obj.read()
                                if(prev_data == url_data):
                                        time.sleep(2)
                                        continue
                                request = True
                                prev_data = url_data
			except:
				time.sleep(5)
				continue
                thr = Threads(func,(url_data,))
		thr.start()
		request = False
		
