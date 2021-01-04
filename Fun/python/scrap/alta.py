import requests
from bs4 import BeautifulSoup
from PIL import Image
import urllib.request


search = 'thinkpad'

response = requests.get(f"https://alta.ge/index.php?subcats=Y&pcode_from_q=Y&pshort=Y&pfull=Y&pname=Y&pkeywords=Y&search_performed=Y&q={search}&dispatch=products.search&items_per_page=25")
soup = BeautifulSoup(response.text, "html.parser")
results = soup.find_all(class_="ty-column3")
print(len(results))

if(len(results) != 0):
    for item in results:
        
        name = item.find(class_="product-title").text
        price = item.find(class_="ty-price-num").text
        currency = item.find(class_="nj-currency-ty-price-num").text
        image = item.find('img')
        image = image['src'].split('?', 1)[0]
        print(name,"-",price,currency,"-",image)

else:
    print("NOTHING!")


# print(response)
# print(soup)
# print(item)