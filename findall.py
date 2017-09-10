#!/usr/bin/env python
# coding=utf-8
//代码执行后就会按照《战争与和平》中人物出场的顺序显示所有人的人名
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)
namelist = bsObj.findAll("span", {"class":"green"})
for name in namelist:
    print(name.get_text())
