import requests

url = "https://iptv-org.github.io/iptv/channels.json"

r = requests.get(url=url)

data = r.json()

for channel in data:
    country = channel['country']['name']
    if (country == 'Georgia'):
        print(channel['url'],' - ',channel['name'])