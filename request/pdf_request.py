import requests, os
API_KEY = 'y42WTaddY2pt7m90tqKW'

# 1. POST /documents
import requests, os
API_KEY     = 'y42WTaddY2pt7m90tqKW'
FILE        = 'sample_1.pdf'
API_URL     = 'http://138.68.102.253:80/documents'
response    = requests.post(API_URL, headers = {'api-key': API_KEY}, files   = {'file': open(FILE, 'rb')})
print('response: ', response)
print('response: ', response.json())

# 2. GET /documents/<DOCUMENT_ID>
API_KEY     = 'y42WTaddY2pt7m90tqKW'
DOCUMENT_ID = '1'
API_URL     = 'http://138.68.102.253:8080/documents/' + DOCUMENT_ID
response    = requests.get(API_URL, headers={'api-key': API_KEY})
response    = response.json()
print('response: ', response)
print('response: ', response.json())

# 3. GET  /documents/<DOCUMENT_ID>/pages/<NUMBER>
API_KEY     = 'y42WTaddY2pt7m90tqKW'
DOCUMENT_ID = '1'
NUMBER      = '1'
API_URL     = 'http://138.68.102.253:8080/documents/' + DOCUMENT_ID + '/pages/' + NUMBER
response    = requests.get(API_URL, headers={'api-key': API_KEY})
response    = response.json()
print('response: ', response)
print('response: ', response.json())



