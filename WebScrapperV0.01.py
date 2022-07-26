import time

import requests
from bs4 import BeautifulSoup
from requests import get
from lxml import etree
import lxml
import cchardet

def scrapXPATH(URL,XPATH):
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
                'Accept-Language': 'en-US, en;q=0.5'})

    PAGE = get(URL, headers=HEADERS)
    WEBCONTENT = BeautifulSoup(PAGE.content, 'html.parser')
    dom = etree.HTML(str(WEBCONTENT))
    value = dom.xpath(XPATH)[0].text
    print(value)

    return value

def scrapXPATH_(URL,XPATH,PARSER):
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
                'Accept-Language': 'en-US, en;q=0.5'})

    PAGE = get(URL, headers=HEADERS)
    WEBCONTENT = BeautifulSoup(PAGE.content, PARSER)
    dom = etree.HTML(str(WEBCONTENT))
    value = dom.xpath(XPATH)[0].text
    print(value)

    return value

def scrapXPATH_S(URL,XPATH,PARSER,SESSION):
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
                'Accept-Language': 'en-US, en;q=0.5'})

    PAGE = SESSION.get(URL, headers=HEADERS)
    WEBCONTENT = BeautifulSoup(PAGE.content, PARSER)
    dom = etree.HTML(str(WEBCONTENT))
    value = dom.xpath(XPATH)[0].text
    print(value)

    return value

def runTest_S():
    URL= 'https://pl.wikipedia.org/wiki/Wiki'
    XPATH = '//*[@id="firstHeading"]'
    PARSER_l = 'lxml'
    PARSER_h = 'html.parser'
    SESSION = requests.Session()
    tic_start = time.perf_counter()

    for x in range(100):
        scrapXPATH_S(URL,XPATH,PARSER_l,SESSION)

    tic_end = time.perf_counter()
    print(f"Downloaded the data in {tic_start - tic_end:0.4f} seconds")
    print(f"Avg time = {(tic_start - tic_end)/100:0.4f} " )

def runTest():
    URL= 'https://pl.wikipedia.org/wiki/Wiki'
    XPATH = '//*[@id="firstHeading"]'
    PARSER_l = 'lxml'
    PARSER_h = 'html.parser'
    tic_start = time.perf_counter()

    for x in range(10):
        scrapXPATH_(URL,XPATH,PARSER_l)

    tic_end = time.perf_counter()
    print(f"Downloaded the data in {tic_start - tic_end:0.4f} seconds")


if __name__ == '__main__':
    runTest_S()
