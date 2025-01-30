import requests
from bs4 import BeautifulSoup


def scrape_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('h3')  # Adjust based on the website structure
    return [article.get_text() for article in articles]


def scrape_moneycontrol():
    return scrape_news("https://www.moneycontrol.com/news/")


def scrape_yahoo_news():
    return scrape_news("https://news.yahoo.com/in/")
