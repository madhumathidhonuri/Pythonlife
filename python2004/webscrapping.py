import requests
import pandas as pd
from bs4 import BeautifulSoup
response=requests.get("https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=e207201c-403d-4940-ab91-f2aa49e3a1d7")
print(response)
soup=BeautifulSoup(response.content,'html.parser')
#print(soup)
names=soup.find_all('div', class_="KzDlHZ")
name=[]
for i in names[0:10]:
    d=i.get_text()
    name.append(d)
print(name)
prices=soup.find_all('div', class_="Nx9bqj _4b5DiR")
price=[]
for i in prices[0:10]:
    d=i.get_text()
    price.append(d)
print(price)
rates=soup.find_all('div', class_="XQDdHH")
rate=[]
for i in rates[0:10]:
    d=i.get_text()
    rate.append(d)
print(rate)
images=soup.find_all('img', class_="DByuf4")
image=[]
for i in images[0:10]:
    d=i['src']
    image.append(d)
print(image)
links=soup.find_all('a', class_="CGtC98")
link=[]
for i in links[0:10]:
    d="https://www.flipkart.com"+i['href']
    link.append(d)
print(link)
df=pd.DataFrame()
df["names"]=name
df["prices"]=price
df["rates"]=rate
df["images"]=image
df["links"]=link
df.to_csv("mobiles.csv")