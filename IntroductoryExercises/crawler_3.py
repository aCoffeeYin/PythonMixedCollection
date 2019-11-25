#中国大学排名定向爬虫

import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):               #输入url信息，输出url的内容
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()        #产生异常信息
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist, html):      #将HTML页面放到ulist
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])


def printUnivList(ulist, num):      #将ulist信息打印出来，num为打印数量
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))
    
def main():
    uinfo = []
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html"
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)    # 20所学校信息
    
main()

    