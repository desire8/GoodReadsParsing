import requests
from bs4 import BeautifulSoup

url = 'http://www.goodreads.com/list/show/24716.Highest_Rated_Books_on_Goodreads_with_at_least_100_ratings_'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'lxml')
topBookList = []

for div in soup.find_all("div", class_="js-tooltipTrigger tooltipTrigger"):
    val = div.find('a').get('title')
    topBookList.append(val)
print(topBookList)
