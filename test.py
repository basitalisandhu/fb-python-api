import unittest
import requests
from unittest.mock import patch, Mock
from utility_functions import get_place_id, get_place_phone_number

class ApiTest(unittest.TestCase):
    API_URL = 'http://localhost:5000/getphonenumber?address='
    addresses = []

    @patch('utility_functions.get_place_id')
    def test_get_place_id(self, mock_get_place_id):
        place_details = [
            {"Sheraton Gateway Los Angeles Hotel": "ChIJWQrR4tS2woARHV9LcAjcw48"},
            {"Hilton Los Angeles Airport": "ChIJ_X2Gq9C2woARP-3L7YtxfWc"},
            {"Sonesta Los Angeles Airport Lax": "ChIJEWOfbNS2woARfvJshRTRp6o"},
            {"redline coffee company": "ChIJvyi_74INkFQRKws19d_Cvtk"},
            {"1": "2"}
        ]
        mock_get_place_id.return_value = Mock()
        mock_get_place_id.return_value.json.return_value = place_details
        place = '1'
        place_id = get_place_id(place)
        self.assertEqual(place_id,place_details[4][place])


    @patch('utility_functions.get_place_phone_number')
    def test_get_place_phone_number(self, mock_get_place_phone_number):
        place_details = [
            {"ChIJWQrR4tS2woARHV9LcAjcw48": "(310) 642-1111"},
            {"ChIJ_X2Gq9C2woARP-3L7YtxfWc": "(310) 410-4000"},
            {"ChIJEWOfbNS2woARfvJshRTRp6o": "(310) 642-7500"},
            {"ChIJvyi_74INkFQRKws19d_Cvtk": "(425) 814-9696"}
        ]
        mock_get_place_phone_number.return_value = Mock()
        mock_get_place_phone_number.return_value.json.return_value = place_details
        place_id = 'ChIJ_X2Gq9C2woARP-3L7YtxfWc'
        place_number = get_place_phone_number(place_id)
        self.assertEqual(place_number,place_details[1][place_id])

    def test_whole_api(self):
        self.addresses = [
            'Sheraton Gateway Los Angeles Hotel','(310) 642-1111'
            'Hilton Los Angeles Airport','(310) 410-4000'
            'Sonesta Los Angeles Airport Lax', '(310) 642-7500'
            'redline coffee company', '(425) 814-9696']
        for address in self.addresses:
            response = requests.get(self.API_URL + address)
            self.assertEqual(response.status_code,200)
            self.assertEqual(len(response.json()),1)


if __name__ == "__main__":
    unittest.main()