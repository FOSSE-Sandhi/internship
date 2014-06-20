#!/usr/bin/env python
import BaseHTTPServer
import urlparse
import urllib
import subprocess
import os
import gviz_api
import scipy
import time

HOST_NAME = "localhost"
PORT_NUMBER = 9000
DIR_PATH = "/home/anoop/IITB/gr-howto2/python"
NUM_VALUES = 50

class Serve(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-type","text/html")
		self.end_headers()
		query_string = urlparse.urlparse(self.path).query
		description = [('Output number','string'),('Result','number')]
		table = gviz_api.DataTable(description)
		res = """
			<html>
	 	 		<head>
	    				<script type="text/javascript" src="https://www.google.com/jsapi"></script>
	    				<script type="text/javascript">
	      					google.load("visualization", "1", {packages:["corechart"]});
	      					google.setOnLoadCallback(drawChart);
	      					function drawChart()
						{
							var data = new google.visualization.DataTable(%(values)s,0.6);
							var options = {
		  						title: 'Square Plot'
								};

							var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
							chart.draw(data, options);
	      					}
	    				</script>
	  			</head>
	  			<body>
					<h1>FLOW GRAPH:</h1><br/>
					<img src=%(path_flow_graph)s alt="flow graph" height="700" width="900" align="middle">
					<h1>PLOT:</h1><br/>
	    				<div id="chart_div" style="width: 1200px; height: 350px;"></div>
	  			</body>
			</html>
	"""

		value = []
		path_flow_graph = ""
		query_string = urllib.unquote(query_string)
		param_list = query_string.split("&")
		param_list.insert(0,"./xmlparse.py")
		if(self.path == DIR_PATH+"/Flow_fs.png" or self.path == DIR_PATH+"/Flow.png"):
			fp = open(self.path,"rb")
			self.wfile.write(fp.read())
		
		elif(self.path.startswith("/fs")):
			param_list.insert(1,"file sink")
			xmlproc = subprocess.Popen(param_list)	
			xmlproc.wait()
			process = subprocess.Popen([DIR_PATH+"/top_block.py"], stdout=subprocess.PIPE)
			time.sleep(2)
			process.kill()
			arr = scipy.fromfile(DIR_PATH + "/output", dtype=scipy.float32, count=NUM_VALUES)
			
			for i in range(NUM_VALUES):
				value.append([str(i),float(arr[i])])
			
			path_flow_graph = DIR_PATH + "/Flow_fs.png"
						
		elif(self.path.startswith("/ps")):
			param_list.insert(1,"plot sink")
			xmlproc = subprocess.Popen(param_list)	
			xmlproc.wait()
			process = subprocess.Popen([DIR_PATH + "/top_block.py"], stdout=subprocess.PIPE)

		        #To eliminate the first two lines
		        process.stdout.readlines(2)
			
			for i in range(NUM_VALUES):
	                        val = process.stdout.readline().strip()
        	                val = val.split(" ")[-1]
                	        val = val.strip("[")
                        	val = val.strip("]")
				value.append([str(i),float(val)])
			process.kill()	
			path_flow_graph = DIR_PATH + "/Flow.png"		
		
		table.AppendData(value)
		values = table.ToJSon(columns_order=('Output number','Result'))
		result = res % vars()
		self.wfile.write(result)

if __name__ == "__main__":
	httpd = BaseHTTPServer.HTTPServer((HOST_NAME,PORT_NUMBER),Serve)
	httpd.serve_forever()

