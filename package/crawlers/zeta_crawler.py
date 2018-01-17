#!/usr/bin/env python3
from ..crawler import Crawler

class ZetaCrawler(Crawler):
	"""Crawling from zeta wiki. 

	"""

	def __init__(self):
		url = super(ZetaCrawler, self).ZETA_URL()
		Crawler.__init__(self, url)

	def get_conference_info(self):
		p = super(ZetaCrawler, self).get_plain_text()
		print(p)