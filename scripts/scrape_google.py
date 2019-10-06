from scraper import url_scraper
import os
import pandas as pd
from models import location_book, init_env
from tqdm import tqdm

def get_search_term(d):
	return ', '.join(['Nankai', d['City'], d['State'], d['Country']])

if __name__ == '__main__':
	init_env.loads()
	uscraper = url_scraper.URLScraper(site='https://www.linkedin.com/in', domain='.com', strict=False, size_return=400)
	for d in tqdm(location_book):
		if d['Population'] < 70000:
			continue
		urls = uscraper.get_urls(get_search_term(d))
		if any(urls):
			init_env.update_linked_urls_cache(urls)
