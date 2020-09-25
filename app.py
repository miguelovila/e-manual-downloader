import urllib.request
import os
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF as pdf_render
from PyPDF2 import PdfFileMerger

emanual_base_url_student = 'https://www.escolavirtual.pt/emanuais-cs/[isbn]-SE-[part]/html5/[isbn]-SE-[part]-lite//OPS/images/page[current_page].svgz'
emanual_base_url_teacher = 'https://www.escolavirtual.pt/emanuais-cs/[isbn]-TE-[part]/html5/[isbn]-TE-[part]-lite//OPS/images/page[current_page].svgz'
isbn = '978-972-0-85336-3'
part = 2
current_page = 1

#emanual_base_url = (emanual_base_url_teacher.replace('[isbn]', isbn.replace('-',''))).replace('[part]','{:02d}'.format(part))
emanual_base_url = (emanual_base_url_student.replace('[isbn]', isbn.replace('-',''))).replace('[part]','{:02d}'.format(part))

pdf_merger = PdfFileMerger()
while True:
    try:
        print('[INFO] Getting page number {:04d}'.format(current_page))
        temp_svg = open('temp.svg','w')
        web_svgz = urllib.request.urlopen(emanual_base_url.replace('[current_page]','{:04d}'.format(current_page)))
        temp_svg.write(web_svgz.read().decode("utf8"))
        web_svgz.close()
        temp_svg.close()
        pdf_drawer = svg2rlg("temp.svg")
        pdf_render.drawToFile(pdf_drawer, 'temp{:04d}.pdf'.format(current_page))
        pdf_merger.append('temp{:04d}.pdf'.format(current_page))
        current_page += 1
    except:
        if current_page == 1:
            print('[ERROR] The e-manual does not exist. Please check ISBN and PART number.')
        else:
            print('[INFO] Finnished downloading all pages.')
            print('[INFO] Merging pdf files.')
            final_pdf = open("E-Manual.pdf", "wb")
            pdf_merger.write(final_pdf)
            pdf_merger.close()
        break
print('[INFO] Clearing temporary files.')
for temp_file in os.listdir('.'):
    if ('temp' in temp_file) and (('.svg' in temp_file) or ('.pdf' in temp_file)):
        os.remove(temp_file)

#Manual Português: 9789720856210
#Caderno Prático Português: 9789720856296

#Manual Matemática: 9789720856463
#Caderno Prático Matemática: 9789720856302