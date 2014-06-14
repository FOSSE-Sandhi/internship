import BaseHTTPServer
import subprocess

PATH_TOP_BLOCK = "/home/anoop/IITB/gr-howto2/python/top_block.py"
HOST_NAME = "localhost"
PORT = 9000
NUM_VALUES = 500

class Handler(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-type","text/html")
		self.end_headers()
		process = subprocess.Popen([PATH_TOP_BLOCK], stdout=subprocess.PIPE)
		result = []
		
		#To eliminate the first two lines
		process.stdout.readlines(2)

		for i in range(NUM_VALUES):
        		value = process.stdout.readline().strip()
        		value = value.split(" ")[-1]
        		value = value.strip("[")
        		value = value.strip("]")
        		result.append(float(value))
		process.kill()
		self.rfile.write(result)

if __name__ == "__main__":
	httpd = BaseHTTPServer.HTTPServer((HOST_NAME,PORT), Handler)
	httpd.serve_forever()
