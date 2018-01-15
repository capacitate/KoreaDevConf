#!/usr/bin/env python3
from ..crawler import Crawler

class ZetaCrawler(Crawler):
	"""Crawling from zeta wiki. 

	"""

	def __init__(self):
		Crawler.__init__(self, super(ZetaCrawler, self).ZETA_URL())

	