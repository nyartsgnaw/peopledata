import time
import re
import os
import numpy as np
from bs4 import BeautifulSoup
from selenium import webdriver
 
def get_urls_from_soup(soup):
	urls = []
	links = []
	tags = ['Cached','Translate this page', 'Similar', 'Account', 'Search', 'Maps', 'YouTube', 'Play', 'News',
			'Gmail', 'Contacts', 'Drive', 'Calendar', 'Google+', 'Translate', 'Photos', 'More',
			'Shopping', 'Finance', 'Docs', 'Books', 'Blogger', 'Hangouts',
			'Keep', 'Saved', 'Even more from Google', 'Sign in',
			'Maps', 'Flights', 'Search settings', 'Languages', 'Turn on SafeSearch', 'Learn more']
	for link in soup.findAll('a', attrs={'href': re.compile("http")}):
		if link.text not in tags:
			if (link.get('title') == None) & (link.get('data-ved') == None):
				url = re.sub('/url\?q\=', '', link.get('href'))
				urls.append(url)
				links.append(link)
	urls = [url.split('&')[0] for url in urls if url.startswith('https://www.linkedin.com/in')]
	return urls
 
def get_target_urls(base_url, driver, size_return=400):
	all_urls = []
	for page_start_id in range(0, 100 * int(np.floor(size_return / 10)), 100):
		urls = []
		ggurl = base_url + '&start=' + str(page_start_id)
		driver.get(ggurl)
		soup = BeautifulSoup(driver.page_source, 'lxml')
		urls = get_urls_from_soup(soup)
		if urls:
			all_urls += urls
			time.sleep(np.random.randint(5, 7))
        if not urls or len(all_urls) > size_return:
                break
	return all_urls

def get_google_url(search_term, start=False, domain='.com', quotes=False):
	search_term = search_term.replace(' ', '%20')
	if quotes:
		search_term = '%22' + search_term + '%22'
	ggurl = 'http://www.google' + domain + '/search?q=' + search_term + '&num=100'
	if start:
		ggurl = ggurl + '&start=' + str(start)
	return ggurl

def get_linkedin_urls(search_term, driver, size_return=400):
	base_url = get_GoogleURL(search_term + ' site:linkedin.com/in',)
	urls = get_target_urls(base_url, driver, size_return=size_return)
	return urls
 
if __name__ == '__main__':
	driver = webdriver.PhantomJS()
	urls = getLinkedinURL('Nankai, Mountainview', driver, size_return=50)
	print(urls)
	driver.close()
