import glog
import time
import re
import os
import numpy as np
from bs4 import BeautifulSoup
from scraper import selenium_scraper

class URLScraper(selenium_scraper.SeleniumScraper):
	def __init__(self, site='https://www.linkedin.com/in', domain='.com', strict=False, size_return=400):
		self.urls = []
		self.soup = None
		self.driver = None
		self.domain = domain
		self.strict = strict
		self.site = site
		self.size_return = size_return        

	def generate_google_api(self, search_term, page_start_id=''):
		search_term = search_term.replace(' ', '%20')
		if self.strict:
			search_term = '%22' + search_term + '%22'
		if self.site:
			search_term += ' site:' + self.site
		ggurl = 'http://www.google' + self.domain + '/search?q=' + search_term + '&num=100'
		if page_start_id:
			ggurl = ggurl + '&start=' + str(page_start_id)
		return ggurl

	def extract_urls(self, url):
		if not self.driver:
			self.init_driver()
		self.driver.get(url)
		# to avoid internet delay
		time.sleep(1)
		self.soup = BeautifulSoup(self.driver.page_source, 'lxml')
		tags = ['Cached','Translate this page', 'Similar', 'Account', 'Search', 'Maps', 'YouTube', 'Play', 'News',
				'Gmail', 'Contacts', 'Drive', 'Calendar', 'Google+', 'Translate', 'Photos', 'More',
				'Shopping', 'Finance', 'Docs', 'Books', 'Blogger', 'Hangouts',
				'Keep', 'Saved', 'Even more from Google', 'Sign in',
				'Maps', 'Flights', 'Search settings', 'Languages', 'Turn on SafeSearch', 'Learn more']
		for link in self.soup.findAll('a', attrs={'href': re.compile("http")}):
			if link.text in tags:
				continue
			if link.get('title') or link.get('data-ved'):
				continue
			token = re.sub('/url\?q\=', '', link.get('href'))
			if token.startswith(self.site):
				self.urls.append(token.split('&')[0])

	def get_urls(self, search_term):
		n_urls = 0
		for page_start_id in range(0, 100 * int(np.floor(self.size_return / 10)), 100):
			ggurl = self.generate_google_api(search_term, page_start_id)
			self.extract_urls(ggurl)
			if n_urls < len(self.urls) and len(self.urls) < self.size_return:
				n_urls = len(self.urls)
				time.sleep(np.random.randint(5, 15))
			else:  
				break
		glog.info('Got {} results from {}'.format(len(self.urls), search_term))
		return self.urls
