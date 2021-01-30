from .persistence import Persistence
from pymongo import MongoClient


class MongoPersistence(Persistence):
	def __init__(self):
		client = MongoClient('localhost', 27017)
		db = client.crawler
		self.__flats = db.flats

	def saveNew(self, data) -> int:
		beforeCount = self.__flats.count()
		for site in data:
			for flat in site:
				result = self.__flats.update_one(
					{'url': flat['url']},
					{'$setOnInsert': flat},
					upsert=True,
				)
		afterCount = self.__flats.count()
		return afterCount - beforeCount
