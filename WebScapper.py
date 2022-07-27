import requests
from bs4 import BeautifulSoup
from requests import get
from lxml import etree
import json

# Scrap one value from one URL
def scrapXPATH(URL,XPATH,SESSION):
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
                'Accept-Language': 'en-US, en;q=0.5'})

    PAGE = SESSION.get(URL, headers=HEADERS)
    WEBCONTENT = BeautifulSoup(PAGE.content, 'lxml')
    dom = etree.HTML(str(WEBCONTENT))
    value = dom.xpath(XPATH)[0].text
    print(value)

    return value


# Scrap multiple values from multiples URLs
def scrapXPATHs(URLs, XPATHs, SESSION):
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
                'Accept-Language': 'en-US, en;q=0.5'})

    values = []

    for URL in URLs:
        print("")
        PAGE = SESSION.get(URL, headers=HEADERS)
        WEBCONTENT = BeautifulSoup(PAGE.content, 'lxml')
        dom = etree.HTML(str(WEBCONTENT))

        for NAME, XPATH in XPATHs.items():

            value = dom.xpath(XPATH)[0].text
            values.append((NAME, value))
            print(NAME, value)

    return values

#Scrap multiple values f

def ScrapWebPages(SESSION):
    f = open('PriceCheckerConfig.json')
    data = json.load(f)

    for instance in data['Instances']:
        print("__________________________________________________________________________________")
        print(instance['InstanceName'])
        scrapXPATHs(instance['URLS'], instance['ItemsToScrapXPATH'], SESSION)



if __name__ == '__main__':

    SESSION = requests.Session()
    ScrapWebPages(SESSION)


