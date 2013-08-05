import webapp2
from google.appengine.ext.appstats import recording
from Controllers import Home1





app = recording.appstats_wsgi_middleware(webapp2.WSGIApplication([
		("/", Home1),
		("/home",Home1)
	], debug=True
))