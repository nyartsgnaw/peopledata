from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from collections import defaultdict
import json
import os

def click_xpath(xpath, driver):
    element = WebDriverWait(driver, timeout=3, poll_frequency=0.05).until(
        EC.visibility_of_element_located((By.XPATH, xpath))
    )
    element.click()

def fill_id(id, text, driver):
    element = WebDriverWait(driver, timeout=3, poll_frequency=0.05).until(
        EC.visibility_of_element_located((By.ID, id))
    )
    element.clear()
    element.send_keys(text)

def parse_linkedin_soup(soup):
    linkedin_data = json.loads(max(soup.strings, key=len).strip('\n').strip())
    data = defaultdict(list)
    for i, x in enumerate(linkedin_data['included']):
        if 'view' not in x['$type'].lower() and 'mini' not in x['$type'].lower():
            data[x['$type']].append(x)
    return data

def init_driver(linkedin_email='511949487@qq.com', linkedin_password='Wifihi123'):
    driver = webdriver.PhantomJS()
    driver.get('https://www.linkedin.com/uas/login')
    fill_id('username', linkedin_email, driver)
    fill_id('password', linkedin_password, driver)
    click_xpath('//button[@type="submit"]', driver)
    return driver

if __name__ == '__main__':
    driver = init_driver()
    input_path = '/tmp/linkedin_profiles/test_google.txt'
    output_path = '/tmp/linkedin_profiles/test.json'
    os.system('mkdir -p {}'.format(os.path.dirname(output_path)))
    with open(output_path, 'w') as write_f:
        with open(input_path) as f:
            for line in f:
                url = line.strip('\n')
                driver.get(url)
                soup = BeautifulSoup(driver.page_source, 'lxml')
                data = parse_linkedin_soup(soup)
                json_data = json.dumps(data, indent=4, sort_keys=True)
                write_f.write(json_data + '\n')
                print(json_data)
                print('\n')
                print('Profile written to local: {} -> {}'.format(url, output_path))
