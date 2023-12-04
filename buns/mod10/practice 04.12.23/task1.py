import requests
import json


response = requests.get('https://swapi.dev/api/starships/10/')
data = json.loads(response.text)


ship_info = {
    'max_atmosphering_speed': data['max_atmosphering_speed'],
    'pilots': [],
    'ship_name': data['name'],
    'starship_class': data['starship_class'],

}


for pilot_url in data['pilots']:
    pilot_response = requests.get(pilot_url)
    pilot_data = pilot_response.json()
    homeworld_response = requests.get(pilot_data['homeworld'])
    homeworld_data = homeworld_response.json()

    pilot_info = {
        'height': pilot_data['height'],
        'homeworld': pilot_data['homeworld'],
        'homeworld_url': pilot_data['homeworld'],
        'mass': pilot_data['mass'],
        'name': pilot_data['name'],
    }
    ship_info['pilots'].append(pilot_info)


print(json.dumps(ship_info, indent=4))


with open('millenium_falcon_info.json', 'w') as file:
    json.dump(ship_info, file, indent=4)
