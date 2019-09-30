# peopledata

### 1.install Firefox [here](https://www.mozilla.org/en-US/firefox/new/)

### 2.initialize environment:
```
# create and activate peopledata environment
conda create -n [ENVIRONMENT_NAME]

# enter the project directory and install python requirements
pip install -r ./init_env/requirements.txt

# install customized packages
pip install -e .
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

a_list_of_profile_dictionaries = []
with open('/tmp/linkedin_profiles/test_linkedin.json') as f:
    for line in f:
        print('{} profiles read'.format(len(a_list_of_profile_dictionaries)))
        a_list_of_profile_dictionaries.append(json.loads(line.split('\n')[0]))
        
```
