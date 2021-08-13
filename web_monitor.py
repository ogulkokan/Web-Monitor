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
import tkinter as tk
import tkinter.scrolledtext as tkst


url="https://www.tcf.gov.tr/PILATES/KURS.html"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text.encode('latin-1')
soup = BeautifulSoup(html_content, "lxml")

base_url = "https://www.tcf.gov.tr/"
announcement_list = soup.findAll('table', {'class': 'arama_tablosu'})

# Create a window object
window = tk.Tk()
window.title('TGF - course tracking app')
window.iconbitmap('./assets/monitoring.ico')

window.geometry('500x500')
window.config(background = "grey")


def send_telegram_message(registration_link, text):
    """Sends message via Telegram"""
    url_registration = "https://api.telegram.org/bot1876022163:AAEk40yvTBg2ImrQ37j9X45zxF1MDxIOIoo/sendMessage?chat_id=-571647453&text={}".format(text)
    url_txt = "https://api.telegram.org/bot1876022163:AAEk40yvTBg2ImrQ37j9X45zxF1MDxIOIoo/sendMessage?chat_id=-571647453&text={}".format(registration_link)
    
    requests.get(url_txt)
    requests.get(url_registration)

# Create an event handler
def start_monitoring():
    for duyuru in announcement_list:
        rows = duyuru.findAll('tr')
        for i in rows[:5]:
            td = i.findAll('td')
            for x in td[1]:
                registration_link = os.path.join(base_url, x['href'])
                _, tail = os.path.split(registration_link)
                text = x.string
                if '1. Kademe Pilates' in x.string and int(tail) > 1191:
                    print(registration_link)
                    print(x.string)
                    send_telegram_message(registration_link, text)
                    textArea.insert(tk.END, registration_link)
                    textArea.insert(tk.END, text)
                    #this creates a new label to the GUI

                else:
                    textArea.insert(tk.END, "There is no new announcement "+ str(datetime.now()) + '\n')
                    
                    print( "There is no new announcement "+ str(datetime.now()))

    # re-run the function in every 2 minutes
    window.after(120000, start_monitoring)

Button1 = tk.Button(window, text ="Start Monitoring", command = start_monitoring, bg='black', fg='white')
Button1.pack()

textArea = tk.Text(window, width=60, height=20, background="yellow")
# textArea.grid(row=2, column=0)
textArea.pack()

scrollbar = tk.Scrollbar(window)
scrollbar.pack(side="right", fill="y")

textArea.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=textArea.yview)


# Run the event loop
window.mainloop()


