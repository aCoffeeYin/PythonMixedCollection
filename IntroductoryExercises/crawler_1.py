#爬取选定的豆瓣图书前20条热门书评

import requests
from bs4 import BeautifulSoup
import re

count = 0
i = 0
s, count_s, count_del = 0, 0, 0
lst_stars = []

r = requests.get('http://book.douban.com/subject/4913064/comments/hot?p=' + str(i+1))
#其中subject/bookid/comments bookid为选择的书名id
soup = BeautifulSoup(r.text, 'lxml')
comments = soup.find_all('span', 'short')
pattern = re.compile('<span class="user-stars allstar(.*?) rating"')
p = re.findall(pattern, r.text)
for item in comments:
    count += 1
    if count > 50:
        count_del += 1
    else:
        print(count, item.string)




