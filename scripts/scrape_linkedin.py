import json
import os
from tqdm import tqdm
from collections import defaultdict
from scraper import linkedin_scraper
from utils import file_cache

if __name__ == '__main__':
    lscraper = linkedin_scraper.LinkedinScraper()
    if not file_cache.cache['linkedin_urls']:
        raise(Exception('Run scrape_google.py first since you don\' have any scraped urls cached at ./data/cache/linkedin_urls.txt'))
    for url in tqdm(file_cache.get_linkedin_urls()):
        linkedin_profiles = {}
        if url in file_cache.cache['linkedin_profiles']:
            continue
        linkedin_profiles[url] = lscraper.get_profile(url)
        if linkedin_profiles[url]:
            file_cache.update_local_json_cache(linkedin_profiles, 'linkedin_profiles')