import requests, os
API_KEY = 'y42WTaddY2pt7m90tqKW'

# 1. POST /documents
file_path   = os.path.join(os.getcwd(), 'sample_1.pdf')
API_URL     = 'http://138.68.102.253:8080/documents'
content     =  open(file_path, 'r').read()
files = {'file': open(file_path, 'rb'), 'file': open(file_path, 'rb')}
response    = requests.post(API_URL, headers={'api-key': API_KEY}, files=files)
print('status: ', response)
response    = response.json()
print('response: ', response)


# BINARY
file_path   = os.path.join(os.getcwd(), 'sample_1.pdf')
API_URL     = 'http://138.68.102.253:8080/documents'
content     =  open(file_path, 'r').read()
response    = requests.post(API_URL, headers={'api-key': API_KEY}, data=content)
print('status: ', response)
response    = response.json()
print('response: ', response)



file_path   = os.path.join(os.getcwd(), 'sample_2.pdf')
API_URL     = 'http://138.68.102.253:8080/documents'
content     =  open(file_path).read()
response    = requests.post(API_URL, headers={'api-key': API_KEY}, data=content)
print('status: ', response)
response    = response.json()
print('response: ', response)



file_path   = os.path.join(os.getcwd(), 'sample_1.txt')
API_URL     = 'http://138.68.102.253:8080/documents'
content     =  open(file_path, 'r').read()
response    = requests.post(API_URL, headers={'api-key': API_KEY}, data=content)
print('status: ', response)
response    = response.json()
print('response: ', response)


# 2. GET /documents/<DOCUMENT_ID>
DOCUMENT_ID = 'ABC'
API_URL = 'http://138.68.102.253:8080/documents/' + DOCUMENT_ID
response    = requests.post(API_URL, headers={'api-key': API_KEY})
print('status: ', response)
response    = response.json()
print('response: ', response)


# 3. GET  /documents/<DOCUMENT_ID>/pages/
DOCUMENT_ID = 'ABC'
PAGE        = '1'
API_URL = 'http://138.68.102.253:8080/documents/pages/' + DOCUMENT_ID + '/' + pages
response    = requests.post(API_URL, headers={'api-key': API_KEY})
print('status: ', response)
response    = response.json()
print('response: ', response)


