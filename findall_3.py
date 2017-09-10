#!/usr/bin/env python
# coding=utf-8
#处理子标签和其他后代标签，后代标签:descendant 
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
for child in bsObj.find("table", {"id":"giftList"}).children:
    print(child)
print("************************************************\n*******************************************")
for sibling in bsObj.find("table", {"id":"giftList"}).tr.next_siblings:
    #处理兄弟标签
    print(sibling)
