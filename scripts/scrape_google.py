from scraper import url_scraper
 
if __name__ == '__main__':
	url_scraper = url_scraper.URLScraper(site='https://www.linkedin.com/in', domain='.com', strict=False, size_return=400)
	urls = url_scraper.get_urls('Nankai, Mountainview')
	print(urls)
	output_path = '/tmp/linkedin_profiles/test_google.txt'
	os.system('mkdir -p {}'.format(os.path.dirname(output_path)))
	with open(output_path, 'w') as f:
		for url in urls:
			f.write(url + '\n')
