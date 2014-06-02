import webapp2
import re
import cgi
import json
from google.appengine.ext import db
import urllib
import os
class MainPage(webapp2.RequestHandler):
    def get(self):
	self.response.headers['Content-Type'] = 'text/plain'
	heat = self.request.get("heat")
	fan = self.request.get("fan")
	print "heat: ",heat
	print "fan: ",fan
	vals = urllib.urlencode({'heat':heat,'fan':fan})
	url = urllib.urlopen("http://localhost:8080/sign",vals)
	#os.system("python server.py")
	#self.redirect("/response")


class Server(webapp2.RequestHandler):
    heat = 0
    fan = 0
    def get(self):
	global heat
	global fan
	self.response.headers['Content-Type'] = 'text/plain'
	res = [heat,fan]
	print "Server get:",res
	self.response.write(json.dumps(res))

    def post(self):
	global heat
	global fan
	heat = int(cgi.escape(self.request.get('heat')))
	fan = int(cgi.escape(self.request.get('fan')))
	print "Heat & fan in server post:",heat,fan	

class Response(webapp2.RequestHandler):
	temp = "No temperature received."
	def post(self):
		global temp
		self.response.headers['Content-type'] = "text/html"
		temp = cgi.escape(self.request.get("temps"))	
		print temp
	def get(self):
		global temp
		self.response.write(temp)

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign',Server),
    ('/response',Response)
], debug=True)

