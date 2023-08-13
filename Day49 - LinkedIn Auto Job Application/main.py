import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3688611371&f_AL=true&geoId=106164952&keywords=react&location=Mumbai%2C+Maharashtra%2C+India&refresh=true")
sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in.click()
time.sleep(3)

email = driver.find_element(By.XPATH, '//*[@id="username"]')
email.send_keys("EMAIL")

password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys("PASSWORD")

submit = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[3]/button')
submit.click()

time.sleep(5)


job_listings = driver.find_elements(By.CLASS_NAME, 'job-card-container__link')

for item in job_listings:
    item.click()
    time.sleep(3)
    save_button = driver.find_element(By.CLASS_NAME, 'jobs-save-button')
    save_button.click()


driver.quit()






