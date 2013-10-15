
#The following is a list of code that was removed from the working application.

#Split Paragraphs into words
'''
def splitParagraphIntoSentences(paragraph):
	///break a paragraph into sentences
	///and return a list
	import re
	# to split by multile characters

	#   regular expressions are easiest (and fastest)
	sentenceEnders = re.compile('[.!?]')
	sentenceList = sentenceEnders.split(paragraph)
	return sentenceList

p = """This is a sentence.  This is an excited sentence! And do you think this is a question?"""
sentences = splitParagraphIntoSentences(p)
for s in sentences:
print s.strip()
'''



#Getting Latest News From Bing
'''
query = urllib.quote(searchQ)
url = "https://api.datamarket.azure.com/Bing/Search/v1/News?Query='%s'&$format=json&$top=5" % query
api_key = base64.b64encode(":FDHMFbTf24DhwD0HcZTlN7dNlbSWiiIB2Cc/tp10K7k")
rpc = urlfetch.create_rpc()
urlfetch.make_fetch_call(rpc,url, headers={"Authorization": "Basic %s" %api_key})
result = rpc.get_result()
print result.status_code
result = json.loads(result.content)


'''

#Extracting Articles using Diffbot
'''
rpcs = []
urls = []
textTitle=[]

for article in result['d']['results']:
	pageurl = article['Url']
	refcom = {'url':pageurl}
	urls.append(refcom)
	token = "39a31e900a5b7a783100556220f3fe35"
	url = "http://www.diffbot.com/api/article?token="+ token + "&url="+pageurl
	rpc = urlfetch.create_rpc(deadline=60)
	urlfetch.make_fetch_call(rpc,url, headers={"Authorization": "Basic %s" %api_key})
	rpcs.append(rpc)
	
for rpc in rpcs:
	result = rpc.get_result()
	print result.status_code
	result = json.loads(result.content)
	refcom = {'title':result['title'],'text':result['text']}
	textTitle.append(refcom)
	
	'''
	
	#Code for a free sentiment api
	'''
	
rpcs2 = []
for article in textTitle:
	payload = []
	payload.append(MultipartParam("text", article['text']))
	data, headers = multipart_encode(payload)
	del headers['Content-Length']
	url = "http://text-processing.com/api/sentiment/"
	rpc = urlfetch.create_rpc()
	urlfetch.make_fetch_call(rpc,url,payload =str().join(data),method = urlfetch.POST,headers = headers)
	rpcs2.append(rpc)
	'''
	

'''
rpcs2 = []
for tweet in result['statuses']:
	payload = []
	payload.append(MultipartParam("text", tweet['text']))
	data, headers = multipart_encode(payload)
	del headers['Content-Length']
	url = "http://text-processing.com/api/sentiment/"
	rpc = urlfetch.create_rpc()
	urlfetch.make_fetch_call(rpc,url,payload =str().join(data),method = urlfetch.POST,headers = headers)
	rpcs2.append(rpc)
'''
