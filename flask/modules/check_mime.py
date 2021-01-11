#pip3 install python-magic
import magic
mime = magic.Magic(mime=True)

def check_mime(file_path):
    return mime.from_file("sample_1.pdf") # 'application/pdf'
# print(example)
# example = mime.from_file("sample_2.pdf") # 'application/pdf'
# print(example)
# example = mime.from_file("convert.sh") 
# print(example)
# example = mime.from_file("check_mime.py") 
# print(example)
