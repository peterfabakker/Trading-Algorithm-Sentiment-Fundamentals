
from google.appengine.api import urlfetch
import urllib
import base64
import json


class Alchemy(object):
	def __init__(self,content):
		self.content = content
	
	def getSentiment(self):
		try:
			rpcs2 = []
			for tweet in self.content['statuses']:
				tt = tweet['text'].encode('utf')
				form_fields = {
		 		"apikey": "a774b58e3c5111910e283381321bf027a1bb460c",
		 		"text": tt,
		 		"outputMode": "json"
				}
				form_data = urllib.urlencode(form_fields)
				url = "http://access.alchemyapi.com/calls/text/TextGetTextSentiment"
				headers={'Content-Type': 'application/x-www-form-urlencoded'}
				rpc = urlfetch.create_rpc()
				urlfetch.make_fetch_call(rpc,url,payload =form_data,method = urlfetch.POST,headers = headers)
				rpcs2.append(rpc)
				
			return rpcs2
					
		except (KeyError,TypeError):
			rpcs2 = []
			for content in self.content:
				tt = content['text'].encode('utf')
				form_fields = {
		 		"apikey": "a774b58e3c5111910e283381321bf027a1bb460c",
		 		"text": tt,
		 		"outputMode": "json"
				}
				form_data = urllib.urlencode(form_fields)
				url = "http://access.alchemyapi.com/calls/text/TextGetTextSentiment"
				headers={'Content-Type': 'application/x-www-form-urlencoded'}
				rpc = urlfetch.create_rpc()
				urlfetch.make_fetch_call(rpc,url,payload =form_data,method = urlfetch.POST,headers = headers)
				rpcs2.append(rpc)
				
			return rpcs2
			
	def extractResults(self,rpcs2,q):
		scores=[]
		counter = 0
		for	rpc in rpcs2:
			result = rpc.get_result()
			print result.status_code
			result = json.loads(result.content)
			label = result['docSentiment']['type']

			try:
				s = result['docSentiment']['score']
			except KeyError:
				s = ""
			try:
				text = self.content['statuses'][counter]['text']
			except (KeyError,TypeError):
				text = self.content[counter]['text']
			try:
				title = self.content[counter]['title']
			except KeyError:
				title = ""
					
			refcom = {'label':result['docSentiment']['type'],'probability':s,'text':text,'title':title,'stock':q}
			scores.append(refcom)
			counter += 1
				
		return scores
			