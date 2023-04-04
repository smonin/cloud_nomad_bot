from bs4 import BeautifulSoup
import random
import json
import requests
import datetime
from fake_useragent import UserAgent


ua = UserAgent()

headers = {
    'accept': 'application/json, text/plain, */*',
    'user-Agent': ua.google,
}

a_name_link_dict = {}

for i in range(1,5):
    url = f'https://habr.com/ru/top/daily/page{i}/'
    req = requests.get(url, headers=headers).text
    soup = BeautifulSoup(req, 'lxml')
    all_articles = soup.find_all('a', class_='tm-title__link')

    for article in all_articles:
        a_name = article.find('span').text
        a_link = f'https://habr.com{article.get("href")}'
        a_name_link_dict[a_name] = a_link

print(a_name_link_dict)