#!/usr/bin/env python
# coding=utf-8
//这段代码会打印giftList表格中所有的产品的数据行
from urllib.request import urlopen
from bs4 import BeautifulSoup

#html = urlopen("http://www.pythonscraping.com/pages/page3.html")
#bsObj = BeautifulSoup(html)
def getTable(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html)
        for child in bsObj.find("table",{"id":"giftList"}).children:
            print(child)
    except AttributeError as e:
        return None
    #return child
getTable("http://www.pythonscraping.com/pages/page3.html")
#print(child)
