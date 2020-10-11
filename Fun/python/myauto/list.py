import json

def append(usd,date):
    with open("list.json", 'r') as json_file:
        data = json.load(json_file)
    
    data['tesla'].append({
        'price': 3100,
        'date': '06/10/2020 21:04'
    })

    with open('list.json', 'w') as outfile:
        json.dump(data, outfile)