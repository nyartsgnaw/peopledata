# peopledata

### 1.install Firefox [here](https://www.mozilla.org/en-US/firefox/new/)
On Ubuntu
```
sudo apt-get update
sudo apt install firefox
```

### 2.initialize environment:
```
export CODEPATH=$HOME/peopledata
bash $CODEPATH/init_env/init.sh
```


### 3. run google URLs scraper

```
python $CODEPATH/scripts/scrape_google.py
```


### 4. run Linkedin scraper (based on results of step3)
```
python $CODEPATH/scripts/scrape_linkedin.py
```

### 5. read in json files
in python terminal
```
import json
import os
with open(os.path.join(os.getenv('CODEPATH'),'data/cache/linkedin_profiles.json')) as f:
    profile_dicts = json.loads(f.read())
```
### add key to use google geocode: https://developers.google.com/maps/documentation/geocoding/start

```
export GOOGLE_API_KEY={YOUR_OWN_KEY_IN_GOOGLE_CLOUD_PLATFORM}

```
