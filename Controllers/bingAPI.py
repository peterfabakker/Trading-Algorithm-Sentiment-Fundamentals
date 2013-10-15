
#Getting Latest News From Bing


from google.appengine.api import urlfetch
import urllib
import base64
import json



class BingAPI(object):
	
	def __init__(self,searchQ,quantity):
		self.searchQ = searchQ
		self.quantity = quantity
	def getArticles(self):
		query = urllib.quote(self.searchQ)
		url = "https://api.datamarket.azure.com/Bing/Search/v1/News?Query='%s'&$format=json&$top=%s" % (query,self.quantity)
		api_key = base64.b64encode(":FDHMFbTf24DhwD0HcZTlN7dNlbSWiiIB2Cc/tp10K7k")
		rpc = urlfetch.create_rpc()
		urlfetch.make_fetch_call(rpc,url, headers={"Authorization": "Basic %s" %api_key})
		result = rpc.get_result()
		print result.status_code
		result = json.loads(result.content)
				
		urls = []
		
		for article in result['d']['results']:
			pageurl = article['Url']
			refcom = {'url':pageurl}
			urls.append(refcom)
			
		return urls
