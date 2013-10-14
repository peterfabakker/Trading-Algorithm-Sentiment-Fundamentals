
#Getting Latest News From Bing


from google.appengine.api import urlfetch


class Bing():
	pass
	'''
	query = urllib.quote(searchQ)
	url = "https://api.datamarket.azure.com/Bing/Search/v1/News?Query='%s'&$format=json&$top=5" % query
	api_key = base64.b64encode(":FDHMFbTf24DhwD0HcZTlN7dNlbSWiiIB2Cc/tp10K7k")
	rpc = urlfetch.create_rpc()
	urlfetch.make_fetch_call(rpc,url, headers={"Authorization": "Basic %s" %api_key})
	result = rpc.get_result()
	print result.status_code
	result = json.loads(result.content)

	rpcs = []
	urls = []
	textTitle=[]

	
	def __repr__(self):
		return self.getPeriod()
	'''