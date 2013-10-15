
from google.appengine.api import urlfetch
import urllib
import base64
import json



class Diffbot(object):
	#Extracting Articles using Diffbot
	#pass the urls of the articles you got from diffbot
	def __init__(self,urls):
		self.urls = urls
		
	token = "39a31e900a5b7a783100556220f3fe35"
	rpcs=[]
	def getText(self):
		textTitle=[]
		for x in self.urls:
			url = "http://www.diffbot.com/api/article?token="+ self.token + "&url="+x['url']
			rpc = urlfetch.create_rpc(deadline=60)
			urlfetch.make_fetch_call(rpc,url, headers={})
			self.rpcs.append(rpc)

		for rpc in self.rpcs:
			result = rpc.get_result()
			print result.status_code
			result = json.loads(result.content)
			refcom = {'title':result['title'],'text':result['text']}
			textTitle.append(refcom)
		
		return textTitle
	
