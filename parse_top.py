import requests
from bs4 import BeautifulSoup
import sqlite3

url = 'http://www.goodreads.com/list/show/24716.Highest_Rated_Books_on_Goodreads_with_at_least_100_ratings_'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'lxml')
topBookList = []
count = 0

for div in soup.find_all("div", class_="js-tooltipTrigger tooltipTrigger"):
    val = div.find('a').get('title')
    tmp = []
    tmp.append(count)
    count +=1
    tmp.append(val)
    topBookList.append(tmp)

db = sqlite3.connect('book_db.db')
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE book_list(id INTEGER PRIMARY KEY, name TEXT)
    ''')

for item in topBookList:
    cursor.execute('insert into book_list values (?,?)',item)

db.commit()
db.close()
