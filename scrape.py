from bs4 import BeautifulSoup
import requests

url = "https://www.toppreise.ch/browse/Computer-accessories/Computer-components/Graphics-cards-accessories/Graphics-cards-c37?q=rx%206800%20xt#d~757.515.680.1200.459.2185.48.73.895.306%2bs~pa%2ba~4"
page = requests.get(url)
print(page)