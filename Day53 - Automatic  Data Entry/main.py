import time
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By

# FETCHING DATA
BASE_URL = "https://www.zillow.com "
ZILLOW_URL = ('https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22users'
              'SearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.3038963'
              '2177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3A'
              'true%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse'
              '%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%'
              '22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D'
              '%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%'
              '22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isList'
              'Visible%22%3Atrue%2C%22mapZoom%22%3A12%7D')

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0",
    "Accept-Language": "en-US,en;q=0.5"
}

content = requests.get(ZILLOW_URL, headers=headers).text
soup = BeautifulSoup(content, "html.parser")
listing_link_elements = soup.find_all("a", class_="property-card-link")
address_elements = soup.find_all("address")
price_elements = soup.select("div .property-card-data span")

all_links = []
for link in listing_link_elements:
    href = link["href"]
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)

address = [address.get_text().split(" | ")[-1] for address in address_elements]
price = [price.get_text().split(" ")[0] for price in price_elements]

# ADDING DATA TO FORM

FORM_URL = 'YOUR GOOGLE FORMS URL'
driver = webdriver.Firefox()


for i in range(len(address)):
    driver.get(FORM_URL)
    time.sleep(2)
    address_element = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_element = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_element = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    submit_button = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    address_element.click()
    address_element.send_keys(address[i])
    price_element.click()
    price_element.send_keys(price[i])
    link_element.click()
    link_element.send_keys(all_links[i])
    submit_button.click()

print("Data Entry Successfull.")
