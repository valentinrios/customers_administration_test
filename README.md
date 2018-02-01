# customers_administration_test

Steps for run the project

1. Install Python 2.7.14 from https://www.python.org/
2. Install Django 1.11.7 with ```pip install Django==1.11.7```
3. Install Django Rest Framework with ```pip install djangorestframework```
4. Install Django oAuth with ```pip install django-oauth-toolkit```
5. Run with ```python manage.py runserver```

Endpoint for request token: http://localhost:8000/o/token/

ClientID: ```2cZi3mlEXxAmdKoI85Q7htCqePKUEklTTylSpnTd```

ClientSecret: ```zVksIS5FEh4EncFntm0ni0IZIlGugW0iZfUH2sbLaPH98PaBltgwnNfNlGC3Y4WZ4aobQUbIJg3CkkyIddNttAO5XKfOlAIlxoqMuM7UaYf9TC1CYTeh8R3sHq3RveOZ```

Example request token:
```
import requests

url = "http://localhost:8000/o/token/"

payload = "grant_type=password&username=admin&password=c0l0mb14%25"
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'Authorization': "Basic MmNaaTNtbEVYeEFtZEtvSTg1UTdodENxZVBLVUVrbFRUeWxTcG5UZDp6VmtzSVM1RkVoNEVuY0ZudG0wbmkwSVpJbEd1Z1cwaVpmVUgyc2JMYVBIOThQYUJsdGd3bk5mTmxHQzNZNFdaNGFvYlFVYklKZzNDa2t5SWRkTnR0QU81WEtmT2xBSWx4b3FNdU03VWFZZjlUQzFDWVRlaDhSM3NIcTNSdmVPWg==",
    'Cache-Control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
```

Example request customers:
```
import requests

url = "http://localhost:8000/customers/"

headers = {
    'Authorization': "Bearer IOig7D86bvORcQNO6n4itZfglHzdk8",
    'Content-Type': "application/json",
    'Cache-Control': "no-cache"
    }

response = requests.request("PUT", url, headers=headers)

print(response.text)
```

Example put request customer:
```
import requests

url = "http://localhost:8000/customer/"

payload = "{\n\t\"country\": 1,\n    \"name\": \"Jhonathan Espinoza\",\n    \"sports\": [1,2]\n}"
headers = {
    'Authorization': "Bearer IOig7D86bvORcQNO6n4itZfglHzdk8",
    'Content-Type': "application/json",
    'Cache-Control': "no-cache"
    }

response = requests.request("PUT", url, data=payload, headers=headers)

print(response.text)
```

Other routes:
```http://localhost:8000/countries/```
```http://localhost:8000/country/```
```http://localhost:8000/sports/```
```http://localhost:8000/sport/```