from data.mongoPersistence import MongoPersistence
from logger import Logger
from notify import Notify
from scraper.scraper import Scraper

# create logger
logger = Logger()

# scrape data
logger.log('Scraping started')
s = Scraper('/home/peter/programming/crawler/settings.json')
data = s.scrape()

# save data
logger.log('Saving flats to DB')
persistence = MongoPersistence()
added = persistence.saveNew(data)
logger.log('New flats saved: {0}'.format(added))

# notify, if any new founds
if added > 0:
	logger.log('Anouncing {0} new flats'.format(added))
	Notify.anounce('New flats: {0}'.format(added))
