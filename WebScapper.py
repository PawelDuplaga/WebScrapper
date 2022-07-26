from bs4 import BeautifulSoup
from requests import get

URL = 'https://www.olx.pl/d/oferty/q-rtx-3070/'

page = get(URL)
#print(page.content)

WebContent = BeautifulSoup(page.content, 'html.parser')
for offer in WebContent.find_all('div', class_="css-19ucd76"):
    print('___________________________________________________________')
    footer1 = offer.find_next('h6', class_="css-v3vynn-Text eu5v0x0")
    footer2 = offer.find_next('p',class_="css-wpfvmn-Text eu5v0x0")
    price = offer.find_next()
    #print(footer1.contents[0])
    #print(footer2.contents[0])
    #print(footer2.find('p',{'data-testid': 'ad-price'}).get('value'))
    print(footer1,'\n',footer2)
    #print(offer)
