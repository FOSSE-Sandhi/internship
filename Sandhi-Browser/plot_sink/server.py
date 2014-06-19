#!/usr/bin/env python
import BaseHTTPServer
import urlparse
import urllib
import subprocess
import os
import gviz_api
import time

HOST_NAME = "localhost"
PORT_NUMBER = 9000
PATH_TOP_BLOCK = "/home/anoop/IITB/gr-howto2/python/top_block.py"
NUM_VALUES = 500

class Serve(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-type","text/html")
		self.end_headers()
		query_string = urlparse.urlparse(self.path).query
		query_string = urllib.unquote(query_string)
		#Gather individual parameters
		param_list = query_string.split("&")
		
		#append filename of xml parsing file
		param_list.insert(0,"./xmlparse.py")
		#print param_list
		xmlproc = subprocess.Popen(param_list)	
		time.sleep(2)
		while(not os.path.exists(PATH_TOP_BLOCK)):
			continue
		xmlproc.kill()
		process = subprocess.Popen([PATH_TOP_BLOCK], stdout=subprocess.PIPE)

                #To eliminate the first two lines
                process.stdout.readlines(2)

		value = process.stdout.readlines(NUM_VALUES)
		process.kill()
		value = map(str.strip,value)
		value = map(lambda x: x.split(" ")[-1], value)
		value = map(lambda x: x.strip("["), value)
		value = map(lambda x: x.strip("]"), value)
                value = map(float, value)
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
    				<div id="chart_div" style="width: 1200px; height: 700px;"></div>
  			</body>
		</html>
"""
		values = ""
		for i in range(50):
			table.AppendData([[str(i),value[i]]])
		values = table.ToJSon(columns_order=('Output number','Result'))
		result = res % vars()
		self.wfile.write(result)
		#os.system("rm "+PATH_TOP_BLOCK)
if __name__ == "__main__":
	httpd = BaseHTTPServer.HTTPServer((HOST_NAME,PORT_NUMBER),Serve)
	httpd.serve_forever()

