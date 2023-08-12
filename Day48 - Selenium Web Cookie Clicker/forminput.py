from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element(By.NAME, "fName")
l_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
signup_button = driver.find_element(By.CLASS_NAME, "btn")

f_name.send_keys("Ayush")
l_name.send_keys("Singh")
email.send_keys("ayush@gmail.com")
signup_button.click()

