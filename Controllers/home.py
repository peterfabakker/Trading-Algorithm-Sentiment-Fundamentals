import os
import datetime
import webapp2
import jinja2
import cgi
from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.api import mail
import urllib
from google.appengine.api import urlfetch

import pprint
import json
from poster.encode import multipart_encode, MultipartParam
import urllib2
import base64

consumer_key = "6hl3xqvrwc5ElShe55hxQ"
consumer_secret = "v0JYb5XHk2HIVNisHWUjuhmOOWgLWrLlP2FXGtuy4"
callback_url = "http://opinionext.appspot.com/"

class Articles(ndb.Model):
	articles = ndb.JsonProperty(repeated=True)
	created = ndb.DateTimeProperty(auto_now_add=True)
	

	

class Home1(webapp2.RequestHandler):

	def get(self):


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
		path = self.request.path

		query = Articles().query().order(-Articles.created)
		query = query.fetch_page(100)

		tmp = "home22.html"



		views = os.path.abspath(os.path.join(__file__, os.path.pardir, "../Views"))
		jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(views))

		template_values = {
				"path": path,
				"query":query
			}
		template = jinja_environment.get_template(tmp)

		self.response.out.write(template.render(template_values))
		

	
	
	def post(self):
		
		text = self.request.get("opinion")
		

		'''
		
		payload = []
		payload.append(MultipartParam("text", text))
		data, headers = multipart_encode(payload)
		del headers['Content-Length']
		url = "http://text-processing.com/api/sentiment/"
		result = urlfetch.fetch(url = url,
			deadline = 50,
			method = urlfetch.POST,
			payload = str().join(data),
			headers = headers
		)
		
		pageurl = "http://www.thenational.ae/"
		url = "http://www.diffbot.com/api/frontpage?token="+ token + "&url="+pageurl +"&format=json"
		
		result2 = urlfetch.fetch(url = url,
			deadline = 50
		)
		
		result2 = json.loads(result2.content)
		print result.content
		print result2.title
		d = feedparser.parse('http://news.google.com/news?q=apple&output=rss')
		print [entry.title for entry in d['entries']
		'''
		
		
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
		
		consumerKey = "6hl3xqvrwc5ElShe55hxQ"
		consumerSecret = "v0JYb5XHk2HIVNisHWUjuhmOOWgLWrLlP2FXGtuy4"
		
		key = consumerKey + ":" + consumerSecret
		
		api_key = base64.b64encode(key)
		
		
		url = "https://api.twitter.com/oauth2/token"
		rpc = urlfetch.create_rpc(deadline=60)
		urlfetch.make_fetch_call(rpc,url,method=urlfetch.POST,headers={"Authorization": "Basic %s" %api_key},payload="grant_type=client_credentials")
		result = rpc.get_result()
		result = json.loads(result.content)
		accessToken = result["access_token"]
		
		
		searchQ = self.request.get("searchQ")
		q = searchQ
		query = urllib.quote(q)
		url = "https://api.twitter.com/1.1/search/tweets.json?q="+ query +"&lang=en"
		rpc = urlfetch.create_rpc()
		urlfetch.make_fetch_call(rpc,url,headers={"Authorization": "bearer %s" %accessToken})
		result = rpc.get_result()
		result = json.loads(result.content)
		tweets = result
		
	
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
			
		scores=[]
		counter = 0
		for	rpc in rpcs2:
			result = rpc.get_result()
			print result.status_code
			result = json.loads(result.content)
			print result
			label = result['label']
			refcom = {'label':result['label'],'probability':result['probability'][label],'tweet':tweets['statuses'][counter]['text'],'stock':q}			
			scores.append(refcom)
			counter += 1
		
		
		articles = Articles()
		articles.articles.append(scores)
		articles.put()
		self.redirect("/home")
		
			
		"""	
		
			client = oauth.TwitterClient(consumer_key, consumer_secret, callback_url)
			self.redirect(client.get_authorization_url())

			additional_params = {
			  q: searchQ,
			}

			result = client.make_request(
			    "https://api.twitter.com/1.1/search/tweets",
			    token=client_token,
			    secret=client_secret,
			    additional_params=additional_params,
			    method=urlfetch.POST)
		
	class CallbackHandler(webapp2.RequestHandler):
		def get(self):
			client = oauth.TwitterClient(consumer_key, consumer_secret, callback_url)
			auth_token = self.request.get("oauth_token")
			auth_verifier = self.request.get("oauth_verifier")
			user_info = client.get_user_info(auth_token, auth_verifier=auth_verifier)
			
			"""
			
		
			
		
		
		
		
		
		
		
		
		
