import requests
from bs4 import BeautifulSoup 

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, features="html.parser")
para_list = soup.find_all('p')
for para in para_list:
    print(para.get_text())