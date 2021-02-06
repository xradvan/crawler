from view import View
from flask import render_template

class IndexView(View):
	def __init__(self, model):
		self.__model = model

	def render(self):
		flats = self.__model.getFlats()

		# average pps
		pps = IndexView.average(flats, 'pps')

		# average area
		area = IndexView.average(flats, 'area')

		# average rooms
		rooms = IndexView.average(flats, 'rooms')

		return render_template('index.html', area=area, pps=pps, flats=flats, rooms=rooms, count=len(flats))


	@staticmethod
	def average(flats, prop):
		sum = 0
		for flat in flats:
			sum += flat[prop]
		return sum / len(flats)
