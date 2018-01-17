#!/usr/bin/env python3
from flask import Flask
from .package.crawlers.zeta_crawler import ZetaCrawler

app = Flask(__name__)

@app.route('/')
def index():
	c = ZetaCrawler()
	print(c.get_conference_info())
	return c.get_plain_text()

if __name__ == '__main__':
	app.run()