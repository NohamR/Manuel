import pdfkit
import re
from pdfkit.api import configuration
from pypdf import PdfMerger
import time
import os
import sys
import shutil
from tkinter import messagebox



def clear(n):
    for i in range(0, n):
        try:
            shutil.rmtree("C:/Users/Noham/Downloads/Manuel/Code/gen/")
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))

        directory = "gen"
        parent_dir = "C:/Users/Noham/Downloads/Manuel/Code/"
        path = os.path.join(parent_dir, directory)
        try:
            os.mkdir(path)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))


toc = time.perf_counter()

wkhtml_path = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltox/bin/wkhtmltopdf.exe")  #by using configuration you can add path value.
# options = {
#     'page-size': 'Letter',
#     'margin-top': '0.75in',
#     'margin-right': '0.75in',
#     'margin-bottom': '0.75in',
#     'margin-left': '0.75in',
#     'custom-header': [
#         ('Accept-Encoding', 'gzip')
#     ],
#     'no-outline': None
# }

options = {}
# clear(2)
id = int(input("Quel est l'id ? "))
edition = input("Quelle est l'édition ? ")
nbpages = int(input("Quel est le nombre de pages ? "))


if edition == 'hachette':
    debuturl = 'https://exobank.hachette-livre.fr/contents/final/'
    finurl = '-fxl/OEBPS/Page_{}.html'
elif (edition == 'hatier') or (edition == 'didier'):
    debuturl = 'https://exobank.hachette-livre.fr/contents/final/'
    finurl = '-fxl/OEBPS/page{}.xhtml?interface=postMessage'
else:
    print("L'édition entrée n'existe pas encore")

url = debuturl + str(id) + finurl
# url = "https://exobank.hachette-livre.fr/contents/final/9782278093472-fxl/OEBPS/page{}.xhtml?interface=postMessage"
output = 'C:/Users/Noham/Downloads/Manuel/Code/gen/pdf{}.pdf'
for offset in range(1, nbpages + 1, 1):
    newurl = url.format(offset)
    print(newurl)
    newoutput = output.format(offset)
    print(str(offset) + "/" + str(nbpages))
    
    try:
        pdfkit.from_url(newurl,
                        newoutput,
                        configuration=wkhtml_path,
                        options=options,
                        verbose=False)

    except:
        pdfkit.from_string("Une erreur est survenue lors de la génération de la page.")
        print("error", newoutput)

pdfs = 'C:/Users/Noham/Downloads/Manuel/Code/gen/pdf{}.pdf'
pdfsnewpdfs = []

for offset in range(386, nbpages + 1, 1):
    newurl = url.format(offset)
    print(newurl)
    newoutput = output.format(offset)
    print(str(offset) + "/" + str(nbpages))

    pdfkit.from_url(newurl, newoutput)

pdfs = '/root/content/Manuel/gen/prof{}.pdf'
pdfsnewpdfs = []

for offset in range(1, nbpages + 1, 1):
    newpdfs = pdfs.format(offset)
    pdfsnewpdfs.append(str(newpdfs))
# print(pdfsnewpdfs)

merger.write("result.pdf")
merger.close()
finmerge = time.perf_counter()

# clear(2)
print(f"Gen pdfs en {finpage - toc:0.4f} secondes")
print(f"Gen pdf unique en {finmerge - debutmerge:0.4f} secondes")
print(f"Tout en {finmerge - toc:0.4f} secondes")
print('DONE')