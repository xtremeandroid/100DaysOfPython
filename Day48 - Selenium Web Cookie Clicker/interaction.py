from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# count_element = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count = count_element.text
# count_element.click()

# all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# all_portals.click()

search_button = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/a/span[1]")
search_button.click()
search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)


# driver.quit()