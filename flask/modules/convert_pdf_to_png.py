from pdf2image import convert_from_path

def convert_pdf_to_png(pdf_id):
    images = convert_from_path(pdf)
    for num, img in images:
        print(num, img )
        img.save(str(num)+".jpg", quality=100)
    







# WAND
# Tried wand, unfortunatly Sample_1 does not work. This is due to the fact that Wand does not repair the broken PDF it seems. Ghostscript might be a better solution. 
# https://stackoverflow.com/questions/43149372/repairing-pdfs-with-damaged-xref-table
# import os
# from wand.image import Image as wi
# pdf = wi(filename="sample_1.pdf", resolution=300)
# pdfImages = pdf.convert("png")
