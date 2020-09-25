import urllib.request
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from PyPDF2 import PdfFileMerger

base_url = 'https://www.escolavirtual.pt/emanuais-cs/[isbn]-SE-02/html5/[isbn]-SE-02-lite//OPS/images/page[current_page].svgz'
#https://www.escolavirtual.pt/emanuais-cs/9789720856463-SE-01/html5/9789720856463-SE-01-lite//OPS/images/page0010.svgz
isbn = '9789720856463'
current_page = 1
current_url= ''
pdf_collection = []

base_url = base_url.replace('[isbn]', isbn)

while True:
    try:
        current_url = base_url.replace('[current_page]','{:04d}'.format(current_page))
        temp_svg = open('temp.svg','w')
        web_svgz = urllib.request.urlopen(current_url)
        temp_svg.write(web_svgz.read().decode("utf8"))
        web_svgz.close()
        temp_svg.close()
        pdf_drawer = svg2rlg("temp.svg")
        renderPDF.drawToFile(pdf_drawer, 'page{:04d}.pdf'.format(current_page))
        pdf_collection.append('page{:04d}.pdf'.format(current_page))
        current_page += 1
    except:
        break

merger = PdfFileMerger()
for pdf in pdf_collection:
    merger.append(pdf)
merger.write("result.pdf")
merger.close() 

"""
f= open("page.svg","w")
fp = urllib.request.urlopen("https://www.escolavirtual.pt/emanuais-cs/9789720850188-SE-01/html5/9789720850188-SE-01-lite//OPS/images/page0320.svgz")
f.write(fp.read().decode("utf8"))
fp.close()
f.close()
drawing = svg2rlg("./page.svg")
renderPDF.drawToFile(drawing, "file1.pdf")

f= open("page.svg","w")
fp = urllib.request.urlopen("https://www.escolavirtual.pt/emanuais-cs/9789720850188-SE-01/html5/9789720850188-SE-01-lite//OPS/images/page0321.svgz")
f.write(fp.read().decode("utf8"))
fp.close()
f.close()
drawing = svg2rlg("./page.svg")
renderPDF.drawToFile(drawing, "file2.pdf")


pdfs = ['file1.pdf', 'file2.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()
"""