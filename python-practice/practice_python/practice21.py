import requests
from bs4 import BeautifulSoup 

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, features="html.parser")
para_list = soup.find_all('p')
file_name = input("Enter a file name: ")
with open(file_name, 'w') as open_file:
    for para in para_list:
        open_file.write(para.get_text())