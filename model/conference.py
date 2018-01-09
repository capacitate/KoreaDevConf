#Python 3.6.2

class Conference(object):
	"""Conference will hold basic information: data, title, and where? 
	following properties:

	Attributes:

	"""

	def __init__(self, title, date, where, who):
		self.title = title
		self.date = date
		self.where = where
		self.who = who
	