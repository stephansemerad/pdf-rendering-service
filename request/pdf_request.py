import requests, os
API_KEY = 'i0cgsdYL3hpeOGkoGmA2TxzJ8LbbU1HpbkZo8B3kFG2bRKjx3V'

# 1. POST /documents
file_path   = os.path.join(os.getcwd(), 'sample_1.pdf')
API_URL     = 'http://127.0.0.1:8000/documents'
content     =  open(file_path, 'r').read()
response    = requests.post(API_URL, headers={'api-key': API_KEY}, data=content).json()
print('response: ', response)


file_path   = os.path.join(os.getcwd(), 'sample_2.pdf')
API_URL     = 'http://127.0.0.1:8000/documents'
content     =  open(file_path).read()
response    = requests.post(API_URL, headers={'api-key': API_KEY}, data=content).json()
print('response: ', response)


import pdfbox
p = pdfbox.PDFBox()
file_path   = os.path.join(os.getcwd(), 'sample_2.pdf')
text = p.extract_text(file_path)
print(text)


import os
from pdf2image import convert_from_path, convert_from_bytes
file_path   = os.path.join(os.getcwd(), 'sample_2.pdf')
images = convert_from_bytes(open(file_path, 'rb').read())





file_path   = os.path.join(os.getcwd(), 'sample_1.txt')
API_URL     = 'http://127.0.0.1:8000/documents'
content     =  open(file_path, 'r').read()
response    = requests.post(API_URL, headers={'api-key': API_KEY}, data=content).json()
print('response: ', response)



# 2. GET /documents/<DOCUMENT_ID>
DOCUMENT_ID = 'ABC'
API_URL = 'http://127.0.0.1:8000/documents/' + DOCUMENT_ID
response = requests.get(API_URL, headers={'api-key': API_KEY}).json()
print('response: ', response)


# 3. GET  /documents/<DOCUMENT_ID>/pages/
DOCUMENT_ID = 'ABC'
PAGE        = '1'
API_URL = 'http://127.0.0.1:8000/documents/pages/' + DOCUMENT_ID + '/' + pages
response = requests.get(API_URL, headers={'api-key': API_KEY}).json()
print('response: ', response)


