from .persistence import Persistence
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from os import path
import urllib

class FirestorePersistence(Persistence):
	def __init__(self, baseDir):
		cred = credentials.Certificate(path.join(baseDir, "data/crawler-e793b-firebase-adminsdk-a5jr2-b069bc4c4a.json"))
		firebase_admin.initialize_app(cred)
		self.__db = firestore.client()

	def saveNew(self, data):
		for site in data:
			for flat in site:
				id = urllib.parse.quote(flat['url'], safe='')
				doc_ref = self.__db.collection(u'flats').document(id)
				doc_ref.set(flat)
