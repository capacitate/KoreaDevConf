import unittest
from app.crawler import Crawler

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
		c = Cralwer("http://google.com")
		p = c.get_plain_text()


if __name__ == '__main__':
	unittest.main()