import time

from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://google.com")
driver.maximize_window()
time.sleep(4)
driver.close()