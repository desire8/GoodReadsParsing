import requests
from bs4 import BeautifulSoup

url = 'http://www.goodreads.com/list'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'lxml')
topBookList = []

for div in soup.find_all("div", class_="listImgs"):
    val = div.find('img').get('title')
    topBookList.append(val)
print(topBookList)
