""" Turkish Gymnastics Federation course announcements tracking application

A simple website monitoring script. If the followed course comes to the list, 
a message is sent automatically with the registration link to the previously created telegram group.

onurgulkokan@gmail.com
2021
"""

# Import requests (to download the page)
from bs4 import BeautifulSoup
import requests
import os
import time
from datetime import datetime


# This is a pretty simple script. The script downloads the homepage of VentureBeat, and if it finds some text, emails me.
# If it does not find some text, it waits 60 seconds and downloads the homepage again.

url="https://www.tcf.gov.tr/PILATES/KURS.html"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text.encode('latin-1')
soup = BeautifulSoup(html_content, "lxml")

base_url = "https://www.tcf.gov.tr/"
announcement_list = soup.findAll('table', {'class': 'arama_tablosu'})


def send_telegram_message(registration_link, text):
    """Sends message via Telegram"""
    url_registration = "https://api.telegram.org/bot1876022163:AAEk40yvTBg2ImrQ37j9X45zxF1MDxIOIoo/sendMessage?chat_id=-571647453&text={}".format(text)
    url_txt = "https://api.telegram.org/bot1876022163:AAEk40yvTBg2ImrQ37j9X45zxF1MDxIOIoo/sendMessage?chat_id=-571647453&text={}".format(registration_link)
    
    requests.get(url_txt)
    requests.get(url_registration)


while True:
    for duyuru in announcement_list:
        rows = duyuru.findAll('tr')
        for i in rows[:5]:
            td = i.findAll('td')
            for x in td[1]:
                registration_link = os.path.join(base_url, x['href'])
                _, tail = os.path.split(registration_link)
                text = x.string
                if '2. Kademe Pilates' in x.string and int(tail) > 1191:
                    print(registration_link)
                    print(x.string)
                    send_telegram_message(registration_link, text)
                else:
                    print( "There is no new announcement "+ str(datetime.now()))
    time.sleep(120)
    continue
