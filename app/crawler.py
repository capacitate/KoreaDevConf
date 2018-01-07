#Python 3.6.2

class Crawler(object):
	"""A crawler will bring html source code from web.
	following properties:

	Attributes:
		url: target url to crawl 
	"""

	def __init__(self, url):
		self.url = url

	