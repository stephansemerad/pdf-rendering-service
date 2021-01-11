import os, json, time, redis
from os import listdir
from os.path import isfile, join
from flask import Flask, request, abort, jsonify, send_from_directory, render_template, Response
from werkzeug.utils import secure_filename
from rq import Queue
from modules.background import background_task
from db.db import * 
from modules.check_mime import *
from modules.convert_pdf_to_png import *

# Redis
# ----------------------------------------------------------------------------------------------
# os.system('rq worker &')
r = redis.Redis()
q = Queue(connection = r)

# Folder Structure
# ----------------------------------------------------------------------------------------------
dir_path                    = os.path.dirname(os.path.realpath(__file__))
PDFS_DIRECTORY              = os.path.join(dir_path, "files/pdfs")
PDFS_DIRECTORY_PROCESSED    = os.path.join(dir_path, "files/pdfs/processed")
IMGS_DIRECTORY              = os.path.join(dir_path, "files/imgs")
FOLDERS                     = [PDFS_DIRECTORY, PDFS_DIRECTORY_PROCESSED, IMGS_DIRECTORY]
TABLES                      = ['pdfs', 'api_keys', 'imgs']

# Index Page
# ----------------------------------------------------------------------------------------------
api = Flask(__name__)
@api.route('/', methods=['GET'])
@api.route('/help', methods=['GET'])
def index(): 
    return render_template('index.html')

# Queue 
# ----------------------------------------------------------------------------------------------
@api.route('/q', methods=['GET'])
def current_q(): 
    return str(len(q))
  
@api.route('/add_q', methods=['GET'])
def add_q(): 
    job = q.enqueue(background_task, '0')
    q_len = len(q)
    return (f'task {job.id} added to queat at {job.enqueued_at}. {q_len} tasks in queue')


# Reset
# ----------------------------------------------------------------------------------------------

@api.route('/reset', methods=['GET'])
def reset(): 
    try:
        for FOLDER in FOLDERS: 
            for file in [f for f in listdir(FOLDER) if isfile(join(FOLDER, f))]:  os.remove(os.path.join(FOLDER, file))
        for TABLE in TABLES: update('''drop table '''+TABLE+'''; ''')
    
        sql_tables = open (os.path.join( os.path.dirname(os.path.realpath(__file__)), 'db/tables.sql' ), "r").read().split(';')
        for sql in sql_tables: insert(sql)

        return api.response_class(response=json.dumps({"OK": "200 - Everything was reset"}),status=200,mimetype='application/json')
    except Exception as e:
        return api.response_class(response=json.dumps({"error":"500  - Internal Server Error "}),status=500,mimetype='application/json')


@api.route('/documents',methods = ['POST', 'GET'])
@api.route('/documents/<document_id>',methods = ['POST', 'GET'])
@api.route('/documents/<document_id>/pages/<number>',methods = ['POST', 'GET'])
def documents(document_id='', number=''):
    print('\n[+] new_request')
    print('----------------------------')
    print('document_id: ', document_id)
    print('number: ', document_id)
    print('headers: ', request.headers)
    print('ip address: ', request.remote_addr)




    if 'api-key' not in request.headers:
        json_data = {"error":"401 - Unauthorized - API Key not received in Header"}
        return api.response_class(response=json.dumps(json_data),status=401,mimetype='application/json')
    else:
        print(request.headers['api-key'])
        sql = '''select api_key from api_keys where api_key = '''+br(request.headers['api-key'])+''';'''
        data = select(sql)
        if data ==[]:
            print('API Key is not Ok')
            json_data = {"error":"401 - Unauthorized - API Key is not valid"}
            return api.response_class(response=json.dumps(json_data),status=401,mimetype='application/json')
        else:
            print('API Key is Ok')
            if request.method == 'POST':
                print('request.method POST')
                print('data: ', request.data)
                print('files: ',request.files)
                print('len: ',len(request.files))
                print('keys: ',request.files.keys())

                # Check how many files were passed
                if len(request.files) > 1: 
                    json_data = {"error":"400 - Bad Request - more than one file is not permitted at this moment"}
                    return api.response_class(response=json.dumps(json_data),status=400,mimetype='application/json')
                
                # # Make sure key 'file' is inside
                if 'file' not in request.files.keys():
                    json_data = {"error":"400 - Bad Request - Key 'file' is missing "}
                    return api.response_class(response=json.dumps(json_data),status=400,mimetype='application/json')
                   
                # Make sure it is a PDF
                print('files: ',request.files['file'].filename)
                print(request.files['file'].filename[-4:])

                if request.files['file'].filename[-4:].lower() != '.pdf':
                    json_data = {"error":"400 - Bad Request - API can only process PDF's at this moment "}
                    return api.response_class(response=json.dumps(json_data),status=400,mimetype='application/json')

                # Insert into DB
                pdf_id = ''
                try:
                    sql = '''insert into pdfs (ip_address, filename, status) values ('''+br(request.remote_addr)+''', '''+br(request.files['file'].filename)+''', '''+br('processing')+''');'''
                    print(sql)
                    pdf_id = insert(sql)
                    print('pdf_id: ', pdf_id)
                except Excetion as e:
                    json_data = {"error":"500  - Internal Server Error "}
                    return api.response_class(response=json.dumps(json_data),status=500,mimetype='application/json')


                # Save the PDF file 
                if pdf_id != '':
                    request.files['file'].save(os.path.join(PDFS_DIRECTORY, secure_filename(str(pdf_id)+'.pdf')))


                # # Add to Redis Processing Queue
                # job = q.enqueue(background_task, pdf_id)
                # print(f'task {job.id} added to queat at {job.enqueued_at}. {q_len} tasks in queue')

                # return the Value 
                json_data = {"id": str(pdf_id)}
                return api.response_class(response=json.dumps(json_data),status=200,mimetype='application/json')
 
                return Response("Accepted", status=202  )
            elif request.method == 'GET':
                print('request.method GET')
                return Response("OK", status=200 )

                sql = '''
                select * from pdfs
                '''
                data = select(sql)
                print(data)


            else:
                json_data = {"error":"400 - Bad Request"}
                return api.response_class(response=json.dumps(json_data),status=400,mimetype='application/json')




if __name__ == "__main__":
    api.run(debug=True, host='0.0.0.0', port=80)
    
