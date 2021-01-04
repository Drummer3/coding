import requests
from bs4 import BeautifulSoup
from PIL import Image
import urllib.request


search = 'thinkpad'

response = requests.get(f"https://pcshop.ge/?s={search}&product_cat=0&post_type=product&orderby=price")
soup = BeautifulSoup(response.text, "html.parser")
results = soup.find_all(class_="product")
print(len(results))

if(len(results) != 0):
    for item in results:
        
        # print(item.prettify())
        name = item.find(class_="woocommerce-loop-product__title").text
        price = item.find('bdi').text
        currency = price[0]
        price = price[1:]
        image = item.find('img')
        image = image['src'][2:]
        print(name,"-",price,currency,"-",image)

else:
    print("NOTHING!")


# print(response)
# print(soup)
# print(item)