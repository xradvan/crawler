from .page import Page
from .nehnutelnostiPost import NehnutelnostiPost
from .flat import FlatFactory

class NehnutelnostiPage(Page):
	def collect(self):
		# find all posts
		rawPagePosts = self.soup.find(id='inzeraty').find_all(class_="advertisement-item")

		results = []
		for pagePost in rawPagePosts:
			# get url of individual post
			url = pagePost.find('a').get('href')
			post = NehnutelnostiPost(url)
			# append flat to result list
			results.append(FlatFactory.create(post))

		return results
