import json
from .pageFactory import PageFactory

class Scraper:
	def __init__(self, name):
		self.setttings = []
		# take sites from settings
		with open(name,'r') as settingsFile:
			self.settings = json.load(settingsFile)

	def scrape(self) -> list:
		# collect all data
		collection = []
		for p in self.settings['harvest']:
			page = PageFactory.create(p['name'], p['url'])
			collection.append(page.collect())
		return collection
