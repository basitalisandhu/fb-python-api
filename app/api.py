from json import loads
import requests
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

with open(f'{ROOT_DIR}/secrets.json', 'r') as file:
  secrets = loads(file.read())


def get_place_id(place_name):
    url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={place_name}&inputtype=textquery&locationbias=circle%3A2000%4047.6918452%2C-122.2226413&fields=formatted_address%2Cname%2Cplace_id&key={secrets['KEY']}"
    response = requests.get( url, headers={}, data={})
    print(response)
    return loads(response.text)['candidates'][0]['place_id']


def get_place_phone_number(place_id):
    url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=name%2Cformatted_phone_number&key={secrets['KEY']}"
    response = requests.get( url, headers={}, data={})
    if 'formatted_phone_number' in loads(response.text)['result']:
        return loads(response.text)['result']['formatted_phone_number']
    else:
        return ''

