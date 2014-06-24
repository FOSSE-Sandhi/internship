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
PATH_TOP_BLOCK = "/home/anoop/IITB/gr-howto2/python/top_block.py"
PATH_FLOW_GRAPH = "/home/anoop/IITB/gr-howto2/python/Flow_fs.png"
OUT_FILE_PATH = "/home/anoop/IITB/gr-howto2/python/output"
NUM_VALUES = 50

class Serve(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-type","text/html")
		self.end_headers()
		query_string = urlparse.urlparse(self.path).query
		if(self.path == PATH_FLOW_GRAPH):
			fp = open(PATH_FLOW_GRAPH,"rb")
			self.wfile.write(fp.read())
		else:
			query_string = urllib.unquote(query_string)
			#Gather individual parameters
			param_list = query_string.split("&")
		
			#append filename of xml parsing file
			param_list.insert(0,"./xmlparse.py")
			xmlproc = subprocess.Popen(param_list)	
			xmlproc.wait()
			process = subprocess.Popen([PATH_TOP_BLOCK], stdout=subprocess.PIPE)
			time.sleep(2)
			process.kill()
			arr = scipy.fromfile(OUT_FILE_PATH,dtype=scipy.float32,count=NUM_VALUES)
			value = []
			for i in range(NUM_VALUES):
				value.append([str(i),float(arr[i])])
			description = [('Output number','string'),('Result','number')]
			table = gviz_api.DataTable(description)
			path_flow_graph = PATH_FLOW_GRAPH
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
			
			table.AppendData(value)
			values = table.ToJSon(columns_order=('Output number','Result'))
			result = res % vars()
			self.wfile.write(result)

if __name__ == "__main__":
	httpd = BaseHTTPServer.HTTPServer((HOST_NAME,PORT_NUMBER),Serve)
	httpd.serve_forever()

