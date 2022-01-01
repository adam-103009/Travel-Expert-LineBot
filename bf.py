import requests
from bs4 import BeautifulSoup
response = requests.get(
    "https://travel.ettoday.net/category/%E5%8F%B0%E5%8C%97/")
soup = BeautifulSoup(response.text, "html.parser")
titles = soup.find_all("h3", itemprop="headline")
for title in titles:
    print(title.select_one("a").getText())
    print(title.select_one("a").get("href"))
