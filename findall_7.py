#!/usr/bin/env python
# coding=utf-8
#对findAll_6.py的改进搜索所有词条链接的链接
from urllib.request import urlopen
from bs4 import BeautifulSoup

import datetime
import random
import re

random.seed(datetime.datetime.now())
def getLink(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html)

    return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href = re.compile("^(/wiki/)((?!:).)*$"))
links = getLink("/wiki/kevin_Bacon")
while len(links)>0:
    newArticleUrl = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticleUrl)
    links = getLink(newArticleUrl)
#一个函数getLink(),可以用维基百科词条/wiki/<词条名称>形式的URL连接作为参数
#然后以同样的形式返回一个列表，里面包括所有的词条连接
#一个主函数，以某个起始词条为参数调用getLink(),再从返回的URL中随机挑选一个此条连接，再调用getLink()，直到我们主动停止或者新的页面上没有词条连接
#程序才停止运行
