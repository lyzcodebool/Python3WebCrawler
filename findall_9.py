#!/usr/bin/env python
# coding=utf-8
#改进findAll_8.py的代码，提取网页中csdn博客的第一段文字，标题，链接

from urllib.request import urlopen
from bs4 import BeautifulSoup

import re
pages = set()
def getIformation(pageUrl):
    global pages
    html = urlopen("http://blog.csdn.net" + pageUrl)
    bsObj = BeautifulSoup(html)

    try:
        print(bsObj.h1)
       #temp = bsObj.find(id = "article_content").findAll("p")[0]
       # print(bsObj.find(id = "hotarticls").find("span").find("a").attrs['href'])
    except AttributeError:
        print("页面缺少一些属性!不过不用担心")

    for link in bsObj.findAll("a", href = re.compile("^(/yaopeng_2005/article/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newpage = link.attrs['href']
                print("*********************\n"+ newpage)
                pages.add(newpage)
                getIformation(newpage)
getIformation("/yaopeng_2005")

