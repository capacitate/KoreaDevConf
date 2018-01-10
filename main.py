#!/usr/bin/env python3
from flask import Flask
from cralwers.zeta_crawler import ZetaCrawler

app = Flask(__name__)

@app.route('/')
def index():
	url = 'https://zetawiki.com/wiki/2017_%EA%B5%AD%EB%82%B4_IT_%EC%BB%A8%ED%8D%BC%EB%9F%B0%EC%8A%A4_%EC%9D%BC%EC%A0%95'
	c = ZetaCrawler(url)
	return c.get_plain_text

if __name__ == '__main__':
	app.run()