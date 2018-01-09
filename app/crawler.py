#!/usr/bin/env python3
import urllib.request

class Crawler(object):
	"""A crawler will bring html source code from web.
	following properties:

	Attributes:
		url: target url to crawl 
	"""

	def __init__(self, url):
		self.url = url

	def get_plain_text(self):
		req = urllib.request.Request(self.url)
		response = urllib.request.urlopen(req)
		the_page = response.read()
		return the_page