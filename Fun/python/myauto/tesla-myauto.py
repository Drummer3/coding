import requests
from bs4 import BeautifulSoup
from datetime import datetime
from list import append

URL = 'https://www.myauto.ge/ka/pr/46490885/iyideba-sedani-tesla-model-3-2019-eleqtro-geo'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'}

page = requests.get(URL, headers=headers)

contents = page.content
soup = BeautifulSoup(contents, 'html.parser')
mydivs = soup.findAll("span", {"class": "car-price"})
usd = mydivs[1].get_text()[:-2]
usd = usd.replace(',','')
date = datetime.now()
date = date.strftime("%d/%m/%Y %H:%M")

append(usd,date)
print("Checked!!! Appended!!!")