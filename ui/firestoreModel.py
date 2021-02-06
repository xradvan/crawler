from model import Model
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from os import path

class FirestoreModel(Model):
	def __init__(self, baseDir):
		cred = credentials.Certificate(path.join(baseDir, "data/crawler-e793b-firebase-adminsdk-a5jr2-b069bc4c4a.json"))
		firebase_admin.initialize_app(cred)
		self.__db = firestore.client()

	def getFlats(self):
		flats = self.__db.collection(u'flats').stream()
		result = []
		for flat in flats:
			result.append(flat.to_dict())
		result.reverse()
		return result
