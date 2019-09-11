from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def click_xpath(xpath):
    element = WebDriverWait(driver, timeout, poll_frequency).until(
        EC.visibility_of_element_located((By.XPATH, xpath))
    )
    element.click()

def fill_id(id, text):
    element = WebDriverWait(driver, timeout=3, poll_frequency=0.05).until(
        EC.visibility_of_element_located((By.ID, id))
    )
    element.clear()
    element.send_keys(text)

driver = webdriver.PhantomJS()
driver.get('https://www.linkedin.com/uas/login')
linkedin_email = '511949487@qq.com'
linkedin_password = 'Wifihi123'
fill_id('username', linkedin_email)
fill_id('password', linkedin_password)
click_xpath('//button[@type="submit"]')

url = 'https://www.linkedin.com/in/weichao-will-chou-04588832'
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'lxml')
