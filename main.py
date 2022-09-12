# import all necessary libraries
from xmlrpc.client import boolean
from bs4 import BeautifulSoup
import requests
import time
import datetime
import csv

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

#    pricenum = price.strip()[1:]

    today = datetime.date.today()

    header = ['Title', 'Price', 'Stock', 'Date']
    data = [title, price, stock, today]

    with open('AmazonWebScrapeDataSet.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    
#    pricenum = bool(pricenum)
#    if(pricenum < 80):
#        send_mail()

#def send_mail():
#    import smtplib
#
#    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
#    server.ehlo()
#    #server.starttls()
#    server.ehlo()
#    server.login('zuhairzuberi13@gmail.com','xxxxxxxxxxxx')
#    
#    subject = "Hey Zuhair the product has got a lower price!!! BUY! BUY! BUY!"
#    body = "The price for TLOU Part I on PS5 has reached $40! https://www.amazon.com/Last-Us-Part-PlayStation-5/dp/B0B3QWRQL8/ref=sr_1_1_sspa?keywords=last+of+us+part+1&qid=1662942717&sprefix=last+of+us+%2Caps%2C108&sr=8-1-spons&ufe=app_do%3Aamzn1.fos.006c50ae-5d4c-4777-9bc0-4513d670b6bc&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzNFdPNDhPTDUzMjkwJmVuY3J5cHRlZElkPUEwMTc5MjMwMVY0MDg5UU9INEhESiZlbmNyeXB0ZWRBZElkPUEwMDE0MTUxMzNZWlIzSVBZRVY0QiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
#   
#    msg = f"Subject: {subject}\n\n{body}"
#    
#    server.sendmail(
#        'zuhairzuberi@gmail.com',
#        msg
#    )

while(True):
    check_priceTLOU()
    time.sleep(5)
