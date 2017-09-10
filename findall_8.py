#!/usr/bin/env python
# coding=utf-8
#一开始，用getLink()处理一个空URL，其实是维基百科的主页，因为在函数里空URL就是http://en.wikipedia.org。然后，遍历首页上每个连接，并检查是否已经在全局变量集合pages里了(已经采集的页面集合)。如果不在，就打印到屏幕上，并把连接加入到pages集合，再用getLink()递归的处理这个连接，上限一般是1000条，因为递归会让栈空间溢出

from urllib.request import urlopen 
from bs4 import BeautifulSoup

import re

pages = set()
def getLink(pageUrl):
    global pages
    #html = urlopen("http://en.wikipedia.org"+pageUrl)
    html = urlopen("http://www.geeksforgeeks.org" + pageUrl)
    bsObj = BeautifulSoup(html)
    for link in bsObj.findAll("a", href = re.compile("^(/tag/)")):
    #for link in bsObj.findAll("a", href = re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #判断这个页面是否在集合里面，不在就是新页面，需要添加到集合中，若果是”旧“页面，则摒弃
                newPageUrl = link.attrs['href']
                print(newPageUrl)
                pages.add(newPageUrl)
                getLink(newPageUrl)
getLink("")
