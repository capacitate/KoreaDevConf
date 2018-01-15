import unittest
from package.crawler import Crawler

class Test(unittest.TestCase):

	def setUp(self):
		pass

	def test_numbers_3_4(self):
		self.assertEqual(3 * 4, 12)

	def test_initiate_crawler(self):
		c = Crawler("url")
		self.assertEqual("url", c.url)

	def test_plain_text_crawler(self):
		c = Crawler("url")

		# 이상한 url을 쓴 경우
		try:
			p = c.get_plain_text()
		except Exception:
			self.assertTrue(True)

		# 제대로 긁어 오는 경우
		c = Crawler("http://google.com")
		p = c.get_plain_text()
		self.assertTrue(b"google" in p)

	def test_ZETA_URL(self):
		c = Crawler("url")
		zeta_url = "https://zetawiki.com/wiki/2017_%EA%B5%AD%EB%82%B4_IT_%EC%BB%A8%ED%8D%BC%EB%9F%B0%EC%8A%A4_%EC%9D%BC%EC%A0%95"
		self.assertEqual(zeta_url, c.ZETA_URL())

	def test_get_conference_info(self):
		pass 
		
if __name__ == '__main__':
	unittest.main()