# fb-python-api
### Clone this project
```
git clone git@github.com:basitalisandhu/fb-python-api.git
```

```
cd fb-python-api
```

## Install required packages
```
pip install requirements.txt
```
## Environment Secrets

To run, the server requires a `secrets.json` file to be present in the root folder.  
The JSON must follow the following format: 
{
    "KEY": ""
}

## To Run Server
```
flask run
```
OR
```
python3 wsgi.py
```
## To Run Tests
To run test with mock
```
python3 -m unittest tests/test_with_mock.py
```
To run test without mock
```
python3 -m unittest tests/test_without_mock.py
```