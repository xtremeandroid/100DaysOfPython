from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article_texts = []
article_links = []

news_articles = soup.find_all('tr', class_='athing')
for article in news_articles:
    title_span = article.find('span', class_='titleline').find('a')
    title_text = title_span.get_text()
    link = title_span.get("href")
    article_texts.append(title_text)
    article_links.append(link)

article_up_votes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_up_votes[0])
print(article_texts[0])
print(article_links[0])

