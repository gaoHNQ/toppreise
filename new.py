from bs4 import BeautifulSoup
import requests
from csv import writer
import datetime
import time

current_time = datetime.datetime.now()
print(current_time)
date_time = [str(current_time.year),
            str(current_time.month),
            str(current_time.day),
            str(current_time.hour),
            str(current_time.minute)]
template = "https://www.toppreise.ch/browse/Computer-accessories/Computer-components/Graphics-cards-accessories/Graphics-cards-c37?q=TEMPLATE#d~757.515.680.346.1200.459.2185.48.73.895.306%2bs~pa%2ba~4"
models = ['rx%206600',
          'rx%206600%20xt',
          'rx%206650%20xt',
          'rx%206700%20xt',
          'rx%206750%20xt',
          'rx%206800',
          'rx%206800%20xt',
          'rx%206900%20xt',
          'rx%206950%20xt',
          'rtx%203060',
          'rtx%203060%20ti',
          'rtx%203070',
          'rtx%203070%20ti',
          'rtx%203080',
          'rtx%203080%20ti',
          'rtx%203090',
          'rtx%203090%20ti',
          'rtx%204080',
          'rtx%204090']
"""
template = "https://www.toppreise.ch/browse/Computer-accessories/Computer-components/Graphics-cards-accessories/Graphics-cards-c37#TEMPLATE%2bd~757.515.680.346.1200.459.2185.48.73.895.306%2ba~4"
models = ['oi~ongff417x14%3asv92886',
          'oi~ongff417x14%3asv91612',
          'oi~ongff417x14%3asv96176',
          'oi~ongff417x14%3asv89280',
          'oi~ongff417x14%3asv96213',
          'oi~ongff417x14%3asv86808',
          'oi~ongff417x14%3asv86814',
          'oi~ongff417x14%3asv87960',
          'oi~ongff417x14%3asv96230',
          'oi~ongff417x14%3asv88206',
          'oi~ongff417x14%3asv87488',
          'oi~ongff417x14%3asv85548',
          'oi~ongff417x14%3asv90637',
          'oi~ongff417x14%3asv85528',
          'oi~ongff417x14%3asv90641',
          'oi~ongff417x14%3asv85505',
          'oi~ongff417x14%3asv95454',
          'oi~ongff417x14%3asv98204',
          'oi~ongff417x14%3asv98225']
"""
urls = []
for i in range(0, len(models)):
    urls.append(template.replace('TEMPLATE', models[i]))
    #print(urls[i])
toWrite = date_time
name = "prices.csv"
with open(name, 'a', encoding='utf8', newline='') as f:
    Writer = writer(f)
    for i in range(0, len(models)):
        lists = []
        page = requests.get(urls[i])
        soup = BeautifulSoup(page.content, 'html.parser')
        t = soup.find_all('div', class_="priceContainer shippingPrice")
        for j in t:
            lists.append(float(j.find('div', class_='Plugin_Price').text.replace('<div class="Plugin_Price"> ', '').replace(' </div>', '').replace('\'', '')))
        lists.sort()
        toWrite.append(lists[0])
        print(models[i].replace('%20', ' ')
        time.sleep(1)
    Writer.writerow(toWrite)
print("complete")
