# import all necessary libraries
from xmlrpc.client import boolean
from bs4 import BeautifulSoup

import requests
import time
import datetime
import csv

import ssl
import smtplib
from email.message import EmailMessage

def check_priceTLOU():
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
    stock = souprefined.find(id= "availability").get_text()
    #print(title)
    #print(price)
    #print(stock)

    title = title.strip()
    price = price.strip()
    stock = stock.strip()
    #print(title)
    #print(price)
    #print(stock)

    pricenum = price.strip()[1:]
    pricenumfloat = float(pricenum)

    today = datetime.date.today()

    header = ['Title', 'Price', 'Stock', 'Date']
    data = [title, price, stock, today]

    with open('AmazonWebScrapeDataSet.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)

    if(pricenumfloat < 60):
        send_mailTLOU()

def send_mailTLOU():
    email_sender = 'projecttesterzuzu@gmail.com'
    password = 'xxxxxxxxxxxxxxxxxx'

    email_receiver = 'projecttesterzuzu@gmail.com'

    subject = "Your Item has decreased in price!!!!"
    body = """
    The following item has decreased in price: TLOU2 is now under $60 !!!!

    Click the link below to buy one!
    https://www.amazon.com/Last-Us-Part-PlayStation-5/dp/B0B3QWRQL8/ref=sr_1_1_sspa?keywords=last+of+us+part+1&qid=1662942717&sprefix=last+of+us+%2Caps%2C108&sr=8-1-spons&ufe=app_do%3Aamzn1.fos.006c50ae-5d4c-4777-9bc0-4513d670b6bc&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzNFdPNDhPTDUzMjkwJmVuY3J5cHRlZElkPUEwMTc5MjMwMVY0MDg5UU9INEhESiZlbmNyeXB0ZWRBZElkPUEwMDE0MTUxMzNZWlIzSVBZRVY0QiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=
    """

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
        smtp.login(email_sender, password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


def check_priceRyzen5600x():
    # Connect to Amazon
    URL = 'https://www.amazon.com/AMD-Ryzen-5600X-12-Thread-Processor/dp/B08166SLDF/ref=sr_1_3?crid=18K2GGNTM5PBY&keywords=ryzen+cpu&qid=1662948815&sprefix=ryzen+cpu%2Caps%2C100&sr=8-3&ufe=app_do%3Aamzn1.fos.f5122f16-c3e8-4386-bf32-63e904010ad0'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL,headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")
    souprefined = BeautifulSoup(soup1.prettify(), "html.parser")
 
    title = souprefined.find(id = "productTitle").get_text()
    price = souprefined.find(id = "mbc-price-1").get_text()
    stock = souprefined.find(id= "availability").get_text()

    title = title.strip()
    price = price.strip()
    stock = stock.strip()

    pricenum = price.strip()[1:]
    pricenumfloat = float(pricenum)

    today = datetime.date.today()

    header = ['Title', 'Price', 'Stock', 'Date']
    data = [title, price, stock, today]

    with open('AmazonWebScrapeDataSet.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)

    if(pricenumfloat < 200):
        send_mail5600x()

def send_mail5600x():
    email_sender = 'projecttesterzuzu@gmail.com'
    password = 'xxxxxxxxxxxxxxxxxx'

    email_receiver = 'projecttesterzuzu@gmail.com'

    subject = "Your Item has decreased in price!!!!"
    body = """
    The following item has decreased in price: AMD Ryzen 5 5600x  is now under $200 !!!!
    
    Click the link below to buy one!
    https://www.amazon.com/AMD-Ryzen-5600X-12-Thread-Processor/dp/B08166SLDF/ref=sr_1_3?crid=18K2GGNTM5PBY&keywords=ryzen+cpu&qid=1662948815&sprefix=ryzen+cpu%2Caps%2C100&sr=8-3&ufe=app_do%3Aamzn1.fos.f5122f16-c3e8-4386-bf32-63e904010ad0    
    """

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
        smtp.login(email_sender, password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


while(True):
    check_priceTLOU()
    check_priceRyzen5600x()
    time.sleep(86400)
