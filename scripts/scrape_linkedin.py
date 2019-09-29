import json
import os
from collections import defaultdict
from scraper import linkedin_scraper


if __name__ == '__main__':
    linkedin_scraper = linkedin_scraper.LinkedinScraper()
    input_path = '/tmp/linkedin_profiles/test_google.txt'
    output_path = '/tmp/linkedin_profiles/test_linkedin.json'
    os.system('mkdir -p {}'.format(os.path.dirname(output_path)))
    with open(output_path, 'w') as write_f:
        with open(input_path) as f:
            for line in f:
                url = line.strip('\n')
                data = linkedin_scraper.get_profile(url)
                write_f.write(json.dumps(data) + '\n')
                print(json.dumps(data, indent=4, sort_keys=True))
                print('\n')
                print('Profile written to local: {} -> {}'.format(url, output_path))