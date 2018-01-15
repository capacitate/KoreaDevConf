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
		# 홈페이지 byte 값 반환
		req = urllib.request.Request(self.url)
		response = urllib.request.urlopen(req)
		the_page = response.read()
		return the_page

	# 자식 클래스들이 오버라이드 해서 쓸 함수
	def get_conference_info(self):
		pass 

	# 크롤링 할 홈페이지 주소 
	def ZETA_URL(self):
		# 제타 위키 홈페이지 주소 반환
		return "https://zetawiki.com/wiki/2017_%EA%B5%AD%EB%82%B4_IT_%EC%BB%A8%ED%8D%BC%EB%9F%B0%EC%8A%A4_%EC%9D%BC%EC%A0%95"