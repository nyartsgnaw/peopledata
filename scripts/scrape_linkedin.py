import json
import os
from collections import defaultdict
from scraper import linkedin_scraper
from tqdm import tqdm
from models import linkedin_urls, init_env, linkedin_profiles

if __name__ == '__main__':
    init_env.loads()
    lscraper = linkedin_scraper.LinkedinScraper()
    if not linkedin_urls:
        raise(Exception('Run scrape_google.py first since you don\' have any scraped urls cached at ./data/cache/linkedin_urls.txt'))
    linkedin_profiles = {}
    for url in tqdm(linkedin_urls):
        data = lscraper.get_profile(url)
        if data:
            linkedin_profiles[url] = data
            init_env.update_linkedin_profiles_cache(linkedin_profiles)