from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

# driver.get("https://www.amazon.in/Samsung-inch-60-1-Computer-Monitor/dp/B08GC8P3YZ")
# price = driver.find_element(By.CLASS_NAME, "a-price-whole")
# print(price.text)

driver.get("https://www.python.org")
event_widget = driver.find_element(By.CLASS_NAME, "event-widget")
dates = event_widget.find_elements(By.TAG_NAME, "time")
titles = event_widget.find_elements(By.CSS_SELECTOR, "li a")
events = {}

for i in range(0, len(dates)):
    events[i] = {
        'time': dates[i].text,
        'name': titles[i].text,
    }

print(events)
driver.quit()
