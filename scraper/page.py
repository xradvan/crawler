import requests
from bs4 import BeautifulSoup

class Page:
	"""
	Base class to represent webpage
	"""
	def __init__(self, url):
		self.url = url
		page = requests.get(url)
		self.soup = BeautifulSoup(page.content, 'html.parser')

	def collect(self):
		"""
		Collect all data
		"""
		raise NotImplementedError
