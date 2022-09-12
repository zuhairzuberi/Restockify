# import all necessary libraries
from bs4 import BeautifulSoup
import requests
import time
import datetime
#import smtplib

# Connect to Amazon

URL = 'https://www.amazon.ca/Last-Us-Part-PlayStation/dp/B0B3QYVDBH/ref=sr_1_1?crid=2I206OQTUAHMP&keywords=the+last+of+us+part+1&qid=1662939975&sprefix=the+la%2Caps%2C105&sr=8-1'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL,headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

print(soup1)
