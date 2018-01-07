#Python 3.6.2
from flask import Flask

app = Flask(__name__)

@app.route('/')
def callCrawler():
	return 'Hello World!'