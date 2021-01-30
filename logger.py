import datetime
import os

class Logger:
	def __init__(self):
		self.__filename = "/home/peter/programming/crawler/log/crawlerlog-{0}.log".format(datetime.datetime.now().strftime("%d%m%y"))

	def log(self, data):
		with open(self.__filename, 'a') as file:
			file.write("{0} {1}\n".format(datetime.datetime.now().strftime("%d/%m/%y %X"), data))
