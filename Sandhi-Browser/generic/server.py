import subprocess
import time
import scipy
import urlparse
import BaseHTTPServer
import gviz_api
import urllib

HOME = "/home/anoop"
dir_dict = {
		"square" : HOME+"/IITB/gr-howto2/python",
		"generic" : HOME+"/generic"
		}
HOST_NAME = "localhost"
PORT_NUMBER = 9000
NUM_VALUES = 50

class PlotSink:
	'''Class to handle plot sinks'''
	def __init__(self,path):
		self.path = path
	
	def process(self,limit):
		'''Get upto limit values from the plot sink and return values to caller'''
		process = subprocess.Popen(self.path, stdout=subprocess.PIPE)
		process.stdout.readlines(2)
		value = []
		for i in range(limit):
			val = process.stdout.readline().strip()
                        val = val.split(" ")[-1]
                        val = val.strip("[")
                        val = val.strip("]")
                        value.append([str(i),float(val)])
                process.kill()
		return value


class FileSink:
	'''Class to handle file sinks'''
	def __init__(self,path,outfile):
		self.path = path
		self.outfile = outfile
	
	def process(self,limit):
		'''Get upto limit values from outfile and return values to caller'''
		process = subprocess.Popen(self.path)
		time.sleep(2)	
		process.kill()
		arr = scipy.fromfile(self.outfile, dtype=scipy.float32, count = limit)
		value = []
		for i in range(limit):
			value.append([str(i),float(arr[i])])
		return value
		
class Server(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-type","text/html")
		self.end_headers()
		#print "Path:",self.path
		graph_title = ""
		if (self.path == "/"):
			fp = open("index.html","r")
			self.wfile.write(fp.read())
			fp.close()
			return
		elif (self.path.startswith("/request")):
			query = urlparse.urlparse(self.path).query
			sink = query.split("&")[0]
			flg = query.split("&")[1]
			sink = sink.split("=")[1]
			flg = flg.split("=")[1]
			fp = open(flg + ".html","r")
			data = fp.read()
			response = data % vars()
			self.wfile.write(response)
			return	
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
                                                                title: '%(graph_title)s'
                                                                };

                                                        var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
                                                        chart.draw(data, options);
                                                }
                                        </script>
                                </head>
                                <body>
                                        <h1>FLOW GRAPH:</h1><br/>
                                        <img src="%(path_flow_graph)s" alt="flow graph" height="700" width="900" align="middle">
                                        <h1>PLOT:</h1><br/>
                                        <div id="chart_div" style="width: 1200px; height: 350px;"></div>
                                </body>
                        </html>
        """
		query_string = urllib.unquote(query_string)
		#print "query_string",query_string
		param_list = query_string.split("&")
		param_list.insert(0,"./xmlparse.py")
		opts = self.path.split("/")
		value = []
		path_flow_graph = ""
		if (self.path.endswith(".png")):
			fp = open(self.path,"rb")
			self.wfile.write(fp.read())
			fp.close()

		if (opts[1] == "ps"):
			#We need to use a plot sink
			directory = ""
			if (opts[2] in dir_dict.keys()):
				directory = dir_dict[opts[2]]
				grc_file = directory + "/"+opts[2]+"ps.grc"
				param_list.insert(1,grc_file)
				xmlproc = subprocess.Popen(param_list)
				xmlproc.wait()
				ps = PlotSink(directory + "/top_block.py")				
				path_flow_graph = directory + "/flowps.png"
				value = ps.process(NUM_VALUES)

		elif (opts[1] == "fs"):
			#We need to use a file sink	
			directory = ""
			if (opts[2] in dir_dict.keys()):
				directory = dir_dict[opts[2]]
				grc_file = directory + "/" + opts[2] + "fs.grc"	
				param_list.insert(1,grc_file)
				xmlproc = subprocess.Popen(param_list)
				xmlproc.wait()
				fs = FileSink(directory + "/top_block.py",directory + "/output")
				path_flow_graph = directory + "/flowfs.png"
				value = fs.process(NUM_VALUES)	
		else:
			self.wfile.write("Option not recognized")
			return
		graph_title = opts[2].capitalize()
		table.AppendData(value)
		values = table.ToJSon(columns_order=('Output number','Result'))
		result = res % vars()
		self.wfile.write(result)

if __name__ == "__main__":
	httpd  = BaseHTTPServer.HTTPServer((HOST_NAME,PORT_NUMBER),Server)
	httpd.serve_forever()
