import requests
import pandas as pd
from bs4 import BeautifulSoup
response=requests.get("https://www.oppo.com/in/smartphones/")
print(response)
soup=BeautifulSoup(response.content,'html.parser')
#print(soup)
bunny=soup.find_all('div',class_="divide-item op-swiper-container load-spu-data")
bunn=[]
for i in bunny[0:10]:
    d=i.get_text()
    bunn.append(i)
print(bunn)
prices=soup.find_all('span',class_="now-price-data ft-body-3-1")
price=[]
for i in prices[0:10]:
    d=i.get_text()
    price.append(i)
print(price)