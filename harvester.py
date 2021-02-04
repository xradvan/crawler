from data.firestorePersistence import FirestorePersistence
from logger import Logger
from notify import Notify
from scraper.scraper import Scraper
from os import path

# base dir path
baseDir = '/home/peter/programming/crawler'

# create logger
logger = Logger(baseDir)

# scrape data
logger.log('Scraping started')
s = Scraper(path.join(baseDir, 'settings.json'))
data = s.scrape()

# save data
persistence = FirestorePersistence(baseDir)
added = persistence.saveNew(data)
logger.log('Scraping finished')
