# WAND
# Tried wand, unfortunatly Sample_1 does not work. This is due to the fact that Wand does not repair the broken PDF it seems. Ghostscript might be a better solution. 
# https://stackoverflow.com/questions/43149372/repairing-pdfs-with-damaged-xref-table
# import os
# from wand.image import Image as wi
# pdf = wi(filename="sample_1.pdf", resolution=300)
# pdfImages = pdf.convert("png")

# for i, img in enumerate(pdfImages.sequence):
#     print(i)
#     i += 1
#     page = wi(image=img)
#     page.save(filename=str(i)+'.jpg')

from pdf2image import convert_from_path
images = convert_from_path('/pdf-rendering-service/request/sample_1.pdf')
for num, img in images:
    img.save(str(num)+".jpg", quality=100)



