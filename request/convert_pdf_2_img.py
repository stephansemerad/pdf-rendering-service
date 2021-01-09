import os
from wand.image import Image as wi

pdf = wi(filename="sample_2.pdf", resolution=300)
pdfImages = pdf.convert("png")

for i, img in enumerate(pdfImages.sequence):
    print(i)
    i += 1
    page = wi(image=img)
    page.save(filename=str(i)+'.jpg')



# file_path   = os.path.join(os.getcwd(), 'sample_1.pdf')
# content     =  open(file_path, 'r').read()
