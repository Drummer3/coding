# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from fbchat import Client
from fbchat.models import Message

def sendDead():
    msgDead = f"ჰეი, სიახლე Covid-19(კორონავირუსი)-ს შესახებ: სამწუხაროდ გარდაცვლილთა რაოდენობა გაიზარდა {difDead}-თ. \n\n * იყო {dead}, გახდა {tmpDead}*"
    client.send(Message(text=msgDead), thread_id=salome_id)
    client.send(Message(text=msgDead), thread_id=gvantsa_id)
    client.send(Message(text=msgDead), thread_id=luka_id)
    client.send(Message(text=msgDead), thread_id=nino_id)

def sendHealthy():
    msgDead = f"ჰეი, სიახლე Covid-19(კორონავირუსი)-ს შესახებ: საბედნიეროდ გამოჯანმრთელებულთა რაოდენობა გაიზარდა {difHealthy}-თ. \n\n * იყო {healthy}, გახდა {tmpHealthy}*"
    client.send(Message(text=msgDead), thread_id=salome_id)
    client.send(Message(text=msgDead), thread_id=gvantsa_id)
    client.send(Message(text=msgDead), thread_id=luka_id)
    client.send(Message(text=msgDead), thread_id=nino_id)

username = "+995591080888"
password = "5LqeYiT89MqT"
salome_id ='100004441952367'
gvantsa_id = '100003324853753'
luka_id = '100006316055945'
nino_id = '100010719397666'
client = Client(username, password)

# Set the URL you want to webscrape from
url = 'https://stopcov.ge/'

case = 1145
healthy = 927
dead = 16

while True:
    # Connect to the URL
    response = requests.get(url)

    # Parse HTML and save to BeautifulSoup object
    soup = BeautifulSoup(response.text, "html.parser")
    klas = soup.find_all(class_="quantity-numver")
    tmpCase = int(klas[0].get_text()[:-3])
    tmpHealthy = int(klas[1].get_text()[:-3])
    tmpDead = int(klas[2].get_text()[:-3])
    print(tmpCase)
    print(tmpDead)
    print(tmpHealthy)
    if tmpDead != dead:
        difDead = tmpDead - dead
        sendDead()
        dead = tmpDead
    
    if tmpHealthy != healthy:
        difHealthy = tmpHealthy - healthy
        sendHealthy()
        healthy = tmpHealthy
    
    time.sleep(1800)

client.logout()