import os
import glog
import pandas as pd
from tqdm import tqdm
from utils import file_cache
from scraper import url_scraper

def get_search_term(d):
	return ', '.join(['\"Nankai\"', d['City'], d['State'], d['Country']])

if __name__ == '__main__':
	uscraper = url_scraper.URLScraper(site='https://www.linkedin.com/in', domain='.com', strict=False, size_return=400)
	for d in tqdm(file_cache.get_location_book()):
		linkedin_urls = {}
		search_term = get_search_term(d)
		if d['Population'] < 70000:
			glog.info('Skipping {} for small population'.format(search_term))
			continue
		if search_term in file_cache.cache['linkedin_urls']:
			glog.info('Skipping searched term {}'.format(search_term))
			continue
		linkedin_urls[search_term] = uscraper.get_urls(search_term)
		if any(linkedin_urls[search_term]):
			file_cache.update_local_json_cache(linkedin_urls, 'linkedin_urls')
