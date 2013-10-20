
from google.appengine.api import urlfetch
import urllib
import base64
import json


class tweets(object):
	def __init__(self,query,accessToken):
		self.query = query
		self.accessToken = accessToken
		
	q = searchQ
	query = urllib.quote(q)
	url = "https://api.twitter.com/1.1/search/tweets.json?q="+ query +"&lang=en"
	rpc = urlfetch.create_rpc()
	urlfetch.make_fetch_call(rpc,url,headers={"Authorization": "bearer %s" %accessToken})
	result = rpc.get_result()
	result = json.loads(result.content)
	tweets = result
	