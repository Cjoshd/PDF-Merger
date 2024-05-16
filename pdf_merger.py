import os 
import PyPDF2 # install PyPDF2 if not present: in terminal type: pip3 install PyPDF2

# create the merger object
merger = PyPDF2.PdfMerger()

# the current  code checks every file in the directory in which this programme runs and merges all existing PDFs in the directory.
# original PDFs will still remain.
for file in os.listdir(os.curdir): 
    if file.endswith('.pdf'):
        with open(file, 'rb') as pdf_file:
            merger.append(file)

merger.write('newfile.pdf')
merger.close()
        
