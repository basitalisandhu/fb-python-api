from flask import Blueprint, jsonify, request
from app.api import get_place_id, get_place_phone_number

main = Blueprint('main', __name__)


@main.route('/getphonenumber', methods = ['GET'])
def getphonenumber():
    try:
        place_name = request.args.get('address', default=None, type=str)
        if place_name:
            result = {
                'formatted_phone_number': get_place_phone_number(place_id=get_place_id(place_name=place_name))
                }
            if result['formatted_phone_number'] == '':
                result = {
                'formatted_phone_number': 'Phone number not found for the given address'
                }    
        else:
            result = {
                'ERROR': 'Please Enter Place Name'
                }
    except:
        pass
    
    return jsonify(result)


