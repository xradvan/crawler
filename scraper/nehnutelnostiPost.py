from .post import Post

class NehnutelnostiPost(Post):
	def getTitle(self):
		return self.soup.find('h1').text.strip()

	def getUrl(self):
		return self.url

	def getPage(self):
		return "nehnutelnosti"

	def getLocation(self):
		return self.soup.find(class_='top--info-location').text.split(',')[0].strip()

	def getPrice(self):
		return self.soup.find(class_='price--main paramNo0').span.text.strip().replace(' ','').replace('€','')

	def getArea(self):
		return self.soup.find(class_='parameter--info').ul.select_one('li:nth-of-type(2)').text.strip().split(' ')[2]

	def getRooms(self):
		return self.soup.find(class_='parameter--info').ul.li.select_one('div:nth-of-type(2)').text.strip().split(' ')[1]
