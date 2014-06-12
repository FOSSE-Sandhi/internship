import gviz_api
import urllib
import time
import sbhs
import BaseHTTPServer
import cgi

#Number of iterations for the loop - to get a stable temperature value
NUM_ITER = 50 

class Server:
	def __init__(self,heat,fan):
		self.heat = heat
		self.fan = fan
		self.temp = 0
		self.sbhs = sbhs.Sbhs()
		fp = open("map_machine_ids.txt","r")
                line = fp.read()
                line = line.strip()
                self.machine_id = line.split("=")[0]
                fp.close()

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

HOST_NAME = "localhost"
PORT_NUMBER = 9000

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	heat = 0
	fan = 0	
	def do_POST(self):
		global heat
		global fan		
		self.send_response(200)
		self.wfile.write("")
		form = cgi.FieldStorage(
            fp=self.rfile, 
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
		heat = int(form['heat'].value)
		fan = int(form['fan'].value)
		
		server = Server(heat,fan)
		server.connect()
	        server.setHeat()
	        server.setFan()
		num_iter = NUM_ITER
		tim = 0
	        description = [('Time','string'),('Temperature','number')]
	        table = gviz_api.DataTable(description)
		print "Entering loop"
		for i in range(NUM_ITER):
                	#temperature = server.getTemp()
			temperature = i
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
		print "Loop terminated"
		server.disconnect()

if __name__ == "__main__":
	httpd = BaseHTTPServer.HTTPServer((HOST_NAME,PORT_NUMBER),RequestHandler)
	httpd.serve_forever()
