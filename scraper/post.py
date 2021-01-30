import requests
from bs4 import BeautifulSoup

class Post:
	"""
	Base class to represent post
	"""
	def __init__(self, url):
		self.url = url
		post = requests.get(url)
		self.soup = BeautifulSoup(post.content, 'html.parser')

	def getTitle(self):
		raise NotImplementedError

	def getUrl(self):
		raise NotImplementedError

	def getPage(self):
		raise NotImplementedError

	def getLocation(self):
		raise NotImplementedError

	def getPrice(self):
		raise NotImplementedError

	def getArea(self):
		raise NotImplementedError

	def getRooms(self):
		raise NotImplementedError
