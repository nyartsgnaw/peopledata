from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.firefox.options import Options
from webdriverdownloader import GeckoDriverDownloader
import os

class SeleniumScraper(object):
    def __init__(self):
        self.driver = None

    def init_driver(self, linkedin_email='', linkedin_password='', proxy_host='', proxy_port=None, headless=True):
        # proxy_host = '186.226.38.166'
        # proxy_port = 8080
        # todo add a proxy scraper to get a list of working proxies
        options = Options()
        options.headless = headless
        profile = webdriver.FirefoxProfile()            
        if proxy_host and proxy_port:
            profile.set_preference("network.proxy.type", 1)
            profile.set_preference("network.proxy.http", proxy_host)
            profile.set_preference("network.proxy.http_port", proxy_port)
            profile.update_preferences()
        if os.path.join(os.getenv('HOME'), 'bin') not in os.getenv('PATH'):
            os.environ['PATH'] = os.getenv('PATH') + ':' + os.path.join(os.getenv('HOME'), 'bin')
        try:
            self.driver = webdriver.Firefox(options=options, firefox_profile=profile)
        except Exception as e:
            self.download_and_install()
            self.driver = webdriver.Firefox(options=options, firefox_profile=profile)
        if linkedin_email and linkedin_password:
            self.driver.get('https://www.linkedin.com/uas/login')
            self.fill_id('username', linkedin_email)
            self.fill_id('password', linkedin_password)
            self.click_xpath('//button[@type="submit"]')

    def download_and_install(self):
        gdd = GeckoDriverDownloader()
        gdd.download_and_install()

    def close_driver(self):
        self.driver.close()

    def click_xpath(self, xpath):
        element = WebDriverWait(self.driver, timeout=3, poll_frequency=0.05).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        element.click()

    def fill_id(self, id, text):
        element = WebDriverWait(self.driver, timeout=3, poll_frequency=0.05).until(
            EC.visibility_of_element_located((By.ID, id))
        )
        element.clear()
        element.send_keys(text)
