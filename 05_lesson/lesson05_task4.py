from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

options = Options()
driver = webdriver.Firefox(options=options)
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/login")
user_name = driver.find_element(By.CSS_SELECTOR, "input#username")
password = driver.find_element(By.CSS_SELECTOR, "input#password")
button = driver.find_element(By.CSS_SELECTOR, "i.fa-sign-in")

user_name.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")
button.click()

info = driver.find_element(By.CSS_SELECTOR, "div#flash")
print(info.text)

driver.quit()
