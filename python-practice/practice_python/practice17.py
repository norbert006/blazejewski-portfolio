import requests
from bs4 import BeautifulSoup 

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, features="html.parser")
title_list = soup.find_all('h3')
for title in title_list:
    print(title.get_text())
