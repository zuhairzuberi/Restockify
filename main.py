# import all necessary libraries
from bs4 import BeautifulSoup
import requests
import time
import datetime
#import smtplib
import csv

# Connect to Amazon
URL = 'https://www.amazon.com/Last-Us-Part-PlayStation-5/dp/B0B3QWRQL8/ref=sr_1_1_sspa?keywords=last+of+us+part+1&qid=1662942717&sprefix=last+of+us+%2Caps%2C108&sr=8-1-spons&ufe=app_do%3Aamzn1.fos.006c50ae-5d4c-4777-9bc0-4513d670b6bc&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzNFdPNDhPTDUzMjkwJmVuY3J5cHRlZElkPUEwMTc5MjMwMVY0MDg5UU9INEhESiZlbmNyeXB0ZWRBZElkPUEwMDE0MTUxMzNZWlIzSVBZRVY0QiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL,headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")
# print(soup1) Test to see if BeautifulSoup is functioning
souprefined = BeautifulSoup(soup1.prettify(), "html.parser")
# print(souprefined)

title = souprefined.find(id = "productTitle").get_text()
price = souprefined.find(id = "priceblock_ourprice").get_text()
stock = souprefined.find(id="availability").get_text()
#print(title)
#print(price)
#print(stock)

title = title.strip()
price = price.strip()
stock = stock.strip()
#print(title)
#print(price)
#print(stock)
