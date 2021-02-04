from .post import Post

class FlatFactory:
	@staticmethod
	def create(post: Post) -> dict:
		"""
		Create a flat represented as dictonary
		"""
		flat = dict()

		title = post.getTitle()
		if len(title) > 0:
			flat.update({'title': title})

		url = post.getUrl()
		if len(url) > 0:
			flat.update({'url': url})

		page = post.getPage()
		if len(page) > 0:
			flat.update({'page': page})

		location = post.getLocation()
		if len(location) > 0:
			flat.update({'location': location})

		price = post.getPrice()
		if len(price) > 0:
			flat.update({'price': float(price)})

		area = post.getArea()
		if len(area) > 0:
			flat.update({'area': float(area)})

		if 'price' in flat.keys() and 'area' in flat.keys():
			pps = flat['price'] / flat['area']
			flat.update({'pps': pps})

		rooms = post.getRooms()
		if len(rooms) > 0:
			flat.update({'rooms': int(rooms)})

		return flat
