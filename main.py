from flask import Flask, jsonify, request
import logging
from utility_functions import get_place_id, get_place_phone_number

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

app = Flask(__name__)


@app.route('/getphonenumber', methods = ['GET'])
def getphonenumber():
    try:
        place_name = request.args.get('address', default=None, type=str)
        if place_name and not place_name.isdecimal():
            result = {
                'formatted_phone_number': get_place_phone_number(place_id=get_place_id(place_name=place_name))
                }
        else:
            result = {
                'ERROR': 'Invalid or empty input'
                }
    except Exception as error:
        logger.exception('Something Went Wrong!', error)
        result = {'ERROR':'SERVER ERROR'}
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)