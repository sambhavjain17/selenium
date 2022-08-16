from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://www.amazon.in/')
time.sleep(5)

searchbtn = driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]')
searchbtn.send_keys("iphone 12")

search = driver.find_element(By.XPATH,'//*[@id="nav-search-submit-button"]')
search.send_keys(Keys.RETURN)

