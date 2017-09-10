#!/usr/bin/env python
# coding=utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup

import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

#获取页面所有内链列表
def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    #找出所有以“/”开头的链接
    for link in bsObj.findAll("a",href = re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks
#获取页面所有外链列表
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    #找出所有以http或者www开头且不包含当前url的连接
    for link in bsObj.findAll("a", href = re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks
def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts
def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html)
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(startingPage)
        return getNextExternalLink(internalLinks[random.randint(0, len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]
def followExternalOnly(startingPage):
    externalLink = getRandomExternalLink("http://oreilly.com")
    print("随机外链："+externalLink)
    followExternalOnly(externalLink)

followExternalOnly("http://oreilly.com")
#上面这个程序从http://oreilly.com开始，然后随机的从外链跳到另一个外链，
#网站首页上并不能一直保证发现外链，这时为了能够发现外链，就需要一种类似前面的案例中使用的采集方法，
#即递归的深入一个网站直到找到一个外链为止。
