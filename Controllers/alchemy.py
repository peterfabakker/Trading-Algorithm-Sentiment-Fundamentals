

try:
	rpcs2 = []
	for tweet in result['statuses']:
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
	
except KeyError:
	
	rpcs2 = []
	for tweet in result['statuses']:
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