import time
from selenium.common import ElementClickInterceptedException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

SIMILAR_ACCOUNT = 'ACCOUNT YOU WANT FOLLOWERS FROM'
USERNAME = 'YOUR USERNAME'
PASSWORD = 'YOUR PASSWORD'


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        username = self.driver.find_element(By.NAME, 'username')
        username.click()
        username.send_keys(USERNAME)

        password = self.driver.find_element(By.NAME, 'password')
        password.click()
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)

    def find_follower(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")
        time.sleep(3)

        modal = self.driver.find_element(By.CSS_SELECTOR, 'div ._aano')
        for i in range(20):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        time.sleep(10)
        i = 0
        modal = self.driver.find_element(By.CSS_SELECTOR, 'div ._aano')
        all_buttons = modal.find_elements(By.CSS_SELECTOR, "div._aacl._aaco._aacw._aad6._aade")

        for button in all_buttons:
            if button.text == 'Following' or button.text == 'Requested':
                continue

            if i >= 60:
                break

            try:
                button.click()
                i += 1
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div[2]/'
                                                                   'div[1]/div/div[2]/div/div/div/div/div/div/button[1]')
                cancel_button.click()
        print(f"Followed {i} People.")


insta_follower = InstaFollower()
insta_follower.login()
insta_follower.find_follower()
insta_follower.follow()

