from flask import Flask, jsonify, request
import requests
from json import loads
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

KEY = 'AIzaSyCDcUmm1LO0yeRVqdPsxo2ku6-weisiWHk'

app = Flask(__name__)

payload={}
headers = {}


def get_place_id(place_name):
    url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={place_name}&inputtype=textquery&locationbias=circle%3A2000%4047.6918452%2C-122.2226413&fields=formatted_address%2Cname%2Cplace_id&key={KEY}"
    response = requests.request("GET", url, headers=headers, data=payload)
    return loads(response.text)['candidates'][0]['place_id']


def get_place_phone_number(place_id):
    url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=name%2Cformatted_phone_number&key={KEY}"
    response = requests.request("GET", url, headers=headers, data=payload)
    if 'formatted_phone_number' in loads(response.text)['result']:
        return loads(response.text)['result']['formatted_phone_number']
    else:
        return ''


@app.route('/getphonenumber', methods = ['GET'])
def getphonenumber():
    try:
        place_name = request.args.get('address', default=None, type=str)
        if place_name and not place_name.isdecimal():
            place_id = get_place_id(place_name=place_name)
            result = {
                'formatted_phone_number': get_place_phone_number(place_id=place_id)
                }
        else:
            result = {
                'ERROR': 'Invalid or empty input'
                }
    except Exception as error:
        logger.exception('Something Went Wrong!', error)
        result = {"ERROR":"SERVER ERROR"}
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)