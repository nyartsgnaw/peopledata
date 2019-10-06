
import pandas as pd
import json
import os
from models import geo_locations, location_book, linkedin_urls, linkedin_profiles

os.system('mkdir -p {}'.format(os.path.join(os.getenv('CODEPATH'), 'data/cache')))

PATH_LINKEDIN_PROFILES = os.path.join(os.getenv('CODEPATH'), 'data/cache', 'linkedin_profiles.json')
PATH_GEO_LOCATIONS = os.path.join(os.getenv('CODEPATH'), 'data/cache', 'geo_locations.json')
PATH_LINKEDIN_URLS = os.path.join(os.getenv('CODEPATH'), 'data/cache', 'linkedin_urls.txt')
PATH_LOCATION_BOOK = os.path.join(os.getenv('CODEPATH'), 'data', 'location_book.csv')

def load_location_book():
	if os.path.isfile(PATH_LOCATION_BOOK):
		data = pd.read_csv(PATH_LOCATION_BOOK).to_dict(orient='record')
		if data:
			location_book.extend(data)

def load_linkedin_urls_cache():
	if os.path.isfile(PATH_LINKEDIN_URLS):
		raw = open(PATH_LINKEDIN_URLS).read() 
		if raw:
			linkedin_urls.extend(list(set(raw.split('\n'))))

#todo: move geo_locations to database
def load_geo_locations_cache():
	if os.path.isfile(PATH_GEO_LOCATIONS):
		raw = open(PATH_GEO_LOCATIONS).read() 
		if raw:
			geo_locations.update(json.loads(raw))
	
#todo: move linkedin_profiles to database
def load_linkedin_profiles_cache():
	if os.path.isfile(PATH_LINKEDIN_PROFILES):
		raw = open(PATH_LINKEDIN_PROFILES).read()
		if raw:
			linkedin_profiles.update(json.loads(raw))

def loads():
	load_location_book()
	load_linkedin_urls_cache()
	load_geo_locations_cache()
	load_linkedin_profiles_cache()

def update_linked_urls_cache(linkedin_urls_new):
	load_linkedin_urls_cache()
	linkedin_urls.extend(linkedin_urls_new)
	with open(PATH_LINKEDIN_URLS, 'w') as f:
		f.write(json.dumps(list(set(linkedin_urls))))

def update_geo_location_cache(geo_locations_new):
	load_geo_locations_cache()
	geo_locations.update(geo_locations_new)
	with open(PATH_GEO_LOCATIONS, 'w') as f:
		f.write(json.dumps(geo_locations))

def update_linkedin_profiles_cache(linkedin_profiles_new):
	load_linkedin_profiles_cache()
	linkedin_profiles.update(linkedin_profiles_new)
	with open(PATH_LINKEDIN_PROFILES, 'w') as f:
		f.write(json.dumps(linkedin_profiles))