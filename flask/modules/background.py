
import sys, time, shutil
from pdf2image import convert_from_path
from PIL import Image
from pathlib import Path
sys.path.append('..')
from db.db import * 

def background_task(pdf_id):
    print('background_task')
    print('pdf_id: ', pdf_id)
    sql = '''
    select filename, status from pdfs where pdf_id = '''+br(pdf_id)+''';
    '''
    data = select(sql)
    if data ==[]:
        return 'Could not find PDF'
    else:
        filename, status = data[0][0], data[0][1]
        print(filename, status)

        parent_path             = Path(os.path.dirname(os.path.realpath(__file__))).parent
        file_path               = os.path.join(parent_path, 'files/pdfs')
        file_path_processed     = os.path.join(parent_path, 'files/pdfs/processed')
        pdf_file_path           = os.path.join(file_path, str(pdf_id)+'.pdf')
        pdf_file_path_processed = os.path.join(file_path_processed, str(pdf_id)+'.pdf')       

        if not os.path.isfile(pdf_file_path):
            return 'Could not find PDF'
        else:
            images = convert_from_path(pdf_file_path)
            img_counter = 0
            for img in images:
                img_counter += 1
                print(img)
                filename    = str(pdf_id) + '_' + str(img_counter) + '.png'
                file_path   = os.path.join(parent_path, 'files/imgs')
                img_path    = os.path.join(file_path, filename)
                
                # I . Save Image

                
                print(img.size)
                img.thumbnail((1200,1600), Image.ANTIALIAS)
                print(img.size)


                img.save(img_path, quality=100)


                # size = (1200, 1600)
                # image = Image.open(source_path)
                # image.thumbnail(size, Image.ANTIALIAS)
                # image.save(dest_path, "JPEG")


                print('img_path: ', img_path)

                # II. Resize Image

                # III. 

                print('img_counter: ', img_counter)
                height, width = '', ''
                sql ='''
                insert into imgs (pdf_id, pdf_page,filename, width, height) 
                select '''+br(pdf_id)+''', '''+br(pdf_id)+''', '''+br(filename)+''', '''+br(height)+''', '''+br(width)+'''
                where not exists ( select * from imgs where filename = '''+br(filename)+''');

                '''
                print(sql)
                # insert(sql)


            # im = Image.open(file)


        # print(pdf_file_path)

    # delay = 2
    # print('Task Running')
    # print(f'simulating {delay} second delay')
    # time.sleep(delay)
    # print(len(n))
    # print('Task Complete')
    # return len(n)

background_task(1)

