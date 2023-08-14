import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PROMISES_DOWN, PROMISED_UP = 70, 70
TWITTER_USERNAME = ''
TWITTER_PASSWORD = ''


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")
        go_button = self.driver.find_element(By.CLASS_NAME, 'start-text')
        go_button.click()

        time.sleep(60)

        down_speed_element = self.driver.find_element(By.XPATH,
                                                 '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]'
                                                 '/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        up_speed_element = self.driver.find_element(By.XPATH,
                                               '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/'
                                               'div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')

        self.down = float(down_speed_element.text)
        self.up = float(up_speed_element.text)

    def tweet_at_provider(self, tweet):
        self.driver.get("https://www.twitter.com")
        time.sleep(2)
        signin_button = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/'
                                                           'div[1]/div/div[3]/div[5]/a/div/span/span')
        signin_button.click()

        time.sleep(2)

        email_input = self.driver.find_element(By.NAME, 'text')
        email_input.send_keys(TWITTER_USERNAME)

        next_button = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/'
                                                         'div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/'
                                                         'div/span/span')
        next_button.click()

        time.sleep(2)

        password_input = self.driver.find_element(By.NAME, 'password')
        password_input.send_keys(TWITTER_PASSWORD)

        password_input.send_keys(Keys.ENTER)

        time.sleep(5)

        tweet_input = self.driver.find_element(By.XPATH, '//div[@role="textbox"]')
        tweet_input.click()
        tweet_input.send_keys(tweet)

        time.sleep(2)

        send_post = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]'
                                                       '/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]'
                                                       '/div/div/div[2]/div[3]/div/span/span')
        send_post.click()

        print("Post Sent Successfully")

    def close_browser(self):
        print("Closing Session")
        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()

if bot.up < PROMISED_UP or bot.down < PROMISES_DOWN:
    message = (f"Dear Broadband Provider, I am Getting Speed : Download - {bot.down} MBPS, Upload - {bot.up} MBPS While"
               f" i was"
               f" promised to"
               f" get minimum {PROMISES_DOWN} MBPS Download Speed and {PROMISED_UP} MBPS Upload Speed")
    bot.tweet_at_provider(message)
else:
    print("Internet is Working Normally....")
    bot.close_browser()

