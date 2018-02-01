# customers_administration_test

Steps for run the project

1. Install Python 2.7.14 from https://www.python.org/
2. Install Django 1.11.7 with ```pip install Django==1.11.7```
3. Install Django Rest Framework with ```pip install djangorestframework```
4. Install Django oAuth with ```pip install django-oauth-toolkit```
5. Run with ```python manage.py runserver```

Endpoint for request token: http://localhost:8000/o/token/
Example request:
```
import requests

url = "http://localhost:8000/o/token/"

payload = "grant_type=password&username=admin&password=c0l0mb14%25"
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'Authorization': "Basic MmNaaTNtbEVYeEFtZEtvSTg1UTdodENxZVBLVUVrbFRUeWxTcG5UZDp6VmtzSVM1RkVoNEVuY0ZudG0wbmkwSVpJbEd1Z1cwaVpmVUgyc2JMYVBIOThQYUJsdGd3bk5mTmxHQzNZNFdaNGFvYlFVYklKZzNDa2t5SWRkTnR0QU81WEtmT2xBSWx4b3FNdU03VWFZZjlUQzFDWVRlaDhSM3NIcTNSdmVPWg==",
    'Cache-Control': "no-cache",
    'Postman-Token': "c2a2dd65-e9b5-8e84-a8d1-6a2af1d979a7"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
```