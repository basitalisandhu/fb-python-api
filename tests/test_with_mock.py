import unittest
import requests
from unittest.mock import patch, Mock
from app.api import get_place_id, get_place_phone_number
from json import loads


class ApiTest(unittest.TestCase):
    API_URL = 'http://localhost:5000/getphonenumber?address='
    addresses = []


    def test_get_place_id(self):
        mock_get_patcher = patch('app.api.requests.get')
        place_details = '{\n   "candidates" : [\n      {\n         "formatted_address" : "6101 W Century Blvd, Los Angeles, CA 90045, United States",\n         "name" : "Sheraton Gateway Los Angeles Hotel",\n         "place_id" : "ChIJWQrR4tS2woARHV9LcAjcw48"\n      }\n   ],\n   "status" : "OK"\n}\n'
        mock_get = mock_get_patcher.start()
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = place_details
        place = "Sheraton Gateway Los Angeles Hotel"
        response = get_place_id(place)
        mock_get_patcher.stop()
        try:
            self.assertEqual(response,'ChIJWQrR4tS2woARHV9LcAjcw48', "Failed! Respose does not match the actual outcome.")
        except AssertionError as error:
            print(error)


    def test_get_place_phone_number(self):
        mock_get_patcher = patch('app.api.requests.get')
        place_details = '{\n   "html_attributions" : [],\n   "result" : {\n      "formatted_phone_number" : "(310) 642-1111",\n      "name" : "Sheraton Gateway Los Angeles Hotel"\n   },\n   "status" : "OK"\n}\n'
        mock_get = mock_get_patcher.start()
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = place_details
        place_id = 'ChIJWQrR4tS2woARHV9LcAjcw48'
        response = get_place_phone_number(place_id)
        mock_get_patcher.stop()
        try:
            self.assertEqual(response,'(310) 642-1111', "Failed! Respose does not match the actual outcome.")
        except AssertionError as error:
            print(error)


    def test_whole_api_with_mock(self):
        place = 'Sheraton Gateway Los Angeles Hotel'
        mock_get_patcher = patch('app.views.get_place_id')
        place_id = 'ChIJWQrR4tS2woARHV9LcAjcw48'
        mock_get = mock_get_patcher.start()
        mock_get.return_value = place_id
        
        mock_get_patcher_2 = patch('app.views.get_place_phone_number')
        place_num = '(310) 642-1111'
        mock_get_2 = mock_get_patcher_2.start()
        mock_get_2.return_value = place_num

        response = requests.get(self.API_URL + place)
        mock_get_patcher.stop()
        mock_get_patcher_2.stop()
        try:
            self.assertEqual(loads(response.text)['formatted_phone_number'],'(310) 642-1111', f"Failed! Wrong phone number for {place}")
            self.assertEqual(len(response.json()),1, "Failed! JSON length must be equal to 1")
        except AssertionError as error:
            print(error)


    def test_whole_api_without_mock(self):
        self.addresses = [
            ['Sheraton Gateway Los Angeles Hotel','(310) 642-1111'],
            ['Hilton Los Angeles Airport','(310) 410-4000'],
            ['Sonesta Los Angeles Airport Lax', '(310) 642-7500'],
            ['redline coffee company', '(425) 361-1777']
            ]
        for address in self.addresses:
            response = requests.get(self.API_URL + address[0])
            try:
                self.assertEqual(loads(response.text)['formatted_phone_number'],address[1], f"Failed! Wrong phone number for {address}")
                self.assertEqual(len(response.json()),1, "Failed! JSON length must be equal to 1")
            except AssertionError as error:
                print(error)


if __name__ == "__main__":
    unittest.main()