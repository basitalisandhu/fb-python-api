import unittest
import requests
from json import loads


class ApiTest(unittest.TestCase):
    API_URL = 'http://localhost:5000/getphonenumber?address='
    addresses = []


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