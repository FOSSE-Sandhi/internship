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
	url = urllib.urlopen("http://localhost:8080/sign",vals)
	#Hardcoded to sleep for 15 seconds : change later if necessary
	time.sleep(180)
	self.redirect("/response")


class Server(webapp2.RequestHandler):
    heat = 0
    fan = 0
    def get(self):
	global heat
	global fan
	self.response.headers['Content-Type'] = 'text/plain'
	res = [heat,fan]
	#print "Server get:",res
	self.response.write(json.dumps(res))

    def post(self):
	global heat
	global fan
	heat = int(cgi.escape(self.request.get('heat')))
	fan = int(cgi.escape(self.request.get('fan')))
	#print "Heat & fan in server post:",heat,fan	


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
    ('/sign',Server),
    ('/response',Response)
], debug=True)

