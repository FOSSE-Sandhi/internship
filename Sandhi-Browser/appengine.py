import webapp2
import cgi
import json
from google.appengine.ext import db
import urllib
import time


class MainPage(webapp2.RequestHandler):
    def get(self):
	self.response.headers['Content-Type'] = 'text/plain'
	heat = self.request.get("heat")
	fan = self.request.get("fan")
	print "heat: ",heat
	print "fan: ",fan
	#print self.request.remote_addr
	vals = urllib.urlencode({'heat':heat,'fan':fan})
	try:
		url = urllib.urlopen("http://localhost:9000",vals)
	except:
		pass
	#Hardcoded to sleep for 2 seconds : change later if necessary
	time.sleep(2)
	self.redirect("/response")


class Response(webapp2.RequestHandler):
	temp = "No temperature received."
	def post(self):
		global temp
		self.response.headers['Content-type'] = "text/html"
		temp = self.request.get("temps")	
		#temp = json.loads(temp)
		temp = urllib.unquote(temp)
		#print temp,type(temp)
	
	def get(self):
		global temp
		self.response.headers['Content-type'] = "text/html"
		self.response.out.write(temp)

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/response',Response)
], debug=True)

