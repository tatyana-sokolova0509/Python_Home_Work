from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

options = Options()
driver = webdriver.Firefox(options=options)
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/inputs")
number = driver.find_element(By.CSS_SELECTOR, "input")
number.send_keys("12345")

number.clear()

number.send_keys("54321")

driver.quit()
