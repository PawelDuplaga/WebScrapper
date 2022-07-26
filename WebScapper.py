from bs4 import BeautifulSoup
from requests import get
from lxml import etree

import cProfile
#cProfile.run(download.main)

URL = 'https://www.olx.pl/d/oferty/q-rtx-3070/'

page = get(URL)
#print(page.content)


WebContent = BeautifulSoup(page.content, 'html.parser')
# for offer in WebContent.find_all('div', class_="css-19ucd76"):
#     print('___________________________________________________________')
#     footer1 = offer.find_next('h6', class_="css-v3vynn-Text eu5v0x0")
#     footer2 = offer.find_next('p',class_="css-wpfvmn-Text eu5v0x0")
#     price = offer.find_next()
#     print(footer1.contents[0])
#     for item in footer2 :
#         if(item.__contains__("zł")):
#             print(item)
    #print(footer2.contents[0])
    #print(footer2.find('p',{'data-testid': 'ad-price'}).get('value'))
    #print(footer1,'\n',footer2)
    #print(offer)
URL_zalando = 'https://www.zalando.pl/9n1m-sense-sense-snake-hoodie-bluza-black-9n021004k-q11.html?size=M'
URL_wiki = 'https://pl.wikipedia.org/wiki/Wiki'

XPATH_zalando_snakeHoodie = '//*[@id="main-content"]/div[1]/div/div/div[2]/x-wrapper-re-1-4/div/div[2]/div/div[1]/div[1]/p[1]'
XPATH_wiki = '//*[@id="firstHeading"]'


def printByURLandXPATH(URL,XPATH):
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

for x in range(100):
    #printByURLandXPATH(URL_zalando,XPATH_zalando_snakeHoodie)
    printByURLandXPATH(URL_wiki,XPATH_wiki)