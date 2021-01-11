
import sys, time
from pdf2image import convert_from_path
from datetime import datetime
from PIL import Image
from pathlib import Path
sys.path.append('..')
from db.db import * 

def background_task(pdf_id):
    print(background_task)
    print('pdf_id', pdf_id)
    try:
        print('/n[background_task]')
        print('pdf_id: ', pdf_id)
        data = select('''select filename, status from pdfs where pdf_id = '''+br(pdf_id)+''' -- and status ='processing' ;''')
        if data ==[]:
            update('''update pdfs set status ='failed', processed_at='''+br(datetime.now())+''' where pdf_id='''+br(pdf_id)+''';''')
        else:
            filename, status = data[0][0], data[0][1]
            parent_path             = Path(os.path.dirname(os.path.realpath(__file__))).parent
            file_path               = os.path.join(parent_path, 'files/pdfs')
            pdf_file_path           = os.path.join(file_path, str(pdf_id)+'.pdf')

            if not os.path.isfile(pdf_file_path):
                update('''update pdfs set status ='failed', processed_at='''+br(datetime.now())+''' where pdf_id='''+br(pdf_id)+''';''')
            else:
                images = convert_from_path(pdf_file_path)
                img_counter = 0
                for img in images:
                    img_counter += 1
                    filename    = str(pdf_id) + '_' + str(img_counter) + '.png'
                    file_path   = os.path.join(parent_path, 'files/imgs')
                    img_path    = os.path.join(file_path, filename)
                    
                    img.thumbnail((1200,1600), Image.ANTIALIAS)
                    img.save(img_path, quality=100)
                    height, width = (img.size)

                    sql ='''
                    insert into imgs (pdf_id, pdf_page,filename, width, height) 
                    select '''+br(pdf_id)+''', '''+br(img_counter)+''', '''+br(filename)+''', '''+br(height)+''', '''+br(width)+'''
                    where not exists ( select * from imgs where filename = '''+br(filename)+''');
                    '''
                    insert(sql)

                update('''update pdfs set status ='done', processed_at='''+br(datetime.now())+''' where pdf_id='''+br(pdf_id)+''';''')
    except Exception as e:
        print(e)
        update('''update pdfs set status ='failed', processed_at='''+br(datetime.now())+''' where pdf_id='''+br(pdf_id)+''';''')
