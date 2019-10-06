
import pandas as pd
import json
import os
from collections import defaultdict

class FileCache(object):
	def __init__(self):
		self.cache_paths = defaultdict(str)
		self.cache = defaultdict(dict)

	def loads(self):
		self.cache_paths['linkedin_profiles'] = os.path.join(os.getenv('CODEPATH'), 'data/cache', 'linkedin_profiles.json')
		self.cache_paths['geo_locations'] = os.path.join(os.getenv('CODEPATH'), 'data/cache', 'geo_locations.json')
		self.cache_paths['linkedin_urls'] = os.path.join(os.getenv('CODEPATH'), 'data/cache', 'linkedin_urls.json')
		self.cache_paths['location_book'] = os.path.join(os.getenv('CODEPATH'), 'data', 'location_book.csv')
		os.system('mkdir -p {}'.format(os.path.join(os.getenv('CODEPATH'), 'data/cache')))
		for cache_name in self.cache_paths:
			self.load_local_json_cache(cache_name)

	def load_local_json_cache(self, cache_name):
		if os.path.isfile(self.cache_paths[cache_name]):
			if '.csv' in self.cache_paths[cache_name]:
				listed_records = pd.read_csv(self.cache_paths[cache_name]).to_dict(orient='record')
				if listed_records:
					self.cache[cache_name] = []
					self.cache[cache_name].extend(listed_records)
			elif '.json' in self.cache_paths[cache_name]:
				raw_text = open(self.cache_paths[cache_name]).read() 
				if raw_text:
					self.cache[cache_name].update(json.loads(raw_text))

	def update_local_json_cache(self, new_data, cache_name):
		self.load_local_json_cache(cache_name)
		self.cache[cache_name].update(new_data)
		with open(self.cache_paths[cache_name], 'w') as f:
			f.write(json.dumps(self.cache[cache_name]))

	def get_linkedin_urls(self):
		return list(set(sum(self.cache['linkedin_urls'].values(), [])))

	def get_location_book(self):
		return self.cache['location_book']

	def get_geo_locations(self):
		return self.cache['geo_locations']