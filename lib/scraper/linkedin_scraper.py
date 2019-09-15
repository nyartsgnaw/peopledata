import json
from collections import defaultdict
from bs4 import BeautifulSoup
from scraper import selenium_scraper


class LinkedinScraper(selenium_scraper.SeleniumScraper):
    def __init__(self, linkedin_email='', linkedin_password=''):
        self.soup = None
        self.driver = None
        self.data = defaultdict(list)
        self.linkedin_email = linkedin_email
        self.linkedin_password = linkedin_password

    def extract_profile(self, url):
        if not self.driver:
            self.init_driver(linkedin_email=self.linkedin_email, linkedin_password=self.linkedin_password)
        self.driver.get(url)
        self.soup = BeautifulSoup(self.driver.page_source, 'lxml')
        linkedin_data = json.loads(max(self.soup.strings, key=len).strip('\n').strip())
        for i, x in enumerate(linkedin_data['included']):
            if 'view' not in x['$type'].lower() and 'mini' not in x['$type'].lower():
                self.data[x['$type']].append(x)

    #todo: write profile class
    def get_profile(self, url):
        self.extract_profile(url)
        return self.data
