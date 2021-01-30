from .nehnutelnostiPage import NehnutelnostiPage

class PageFactory:
	@staticmethod
	def create(name, url):
		if name == "nehnutelnosti":
			return NehnutelnostiPage(url)
		else:
			raise NotImplementedError
