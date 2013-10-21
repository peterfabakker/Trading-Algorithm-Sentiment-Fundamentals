
from google.appengine.api import urlfetch
import urllib
import base64
import json


class Tweets(object):
	def __init__(self,q,accessToken):
		self.q = q
		self.accessToken = accessToken
	def getTweets(self):
		q = self.q
		query = urllib.quote(q)
		url = "https://api.twitter.com/1.1/search/tweets.json?q="+ query +"&lang=en"
		rpc = urlfetch.create_rpc()
		urlfetch.make_fetch_call(rpc,url,headers={"Authorization": "bearer %s" %self.accessToken})
		result = rpc.get_result()
		tweets = json.loads(result.content)
	
		return tweets