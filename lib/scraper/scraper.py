from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class SeleniumScraper(object):
    def __init__(self):
        self.driver = None

    def init_driver(self, linkedin_email='', linkedin_password=''):
        self.driver = webdriver.PhantomJS()
        if linkedin_email and linkedin_password:
            self.driver = webdriver.PhantomJS()
            self.driver.get('https://www.linkedin.com/uas/login')
            self.fill_id('username', linkedin_email)
            self.fill_id('password', linkedin_password)
            self.click_xpath('//button[@type="submit"]')

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