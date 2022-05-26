from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
import glob
from pdfminer.high_level import extract_text
import os 

def main():
  
    
    pdf_files = glob.glob(f'SeparateBallots/*.pdf')
    
    count = 0
    for file in pdf_files:
        reader = PdfFileReader(open(file, 'rb'))
        for page in reader.pages:
            writer = PdfFileWriter()
            writer.addPage(page)
            with open(f'sep/output{count}.pdf', 'wb') as out:
                writer.write(out)
            count += 1
    
    pdf_files = glob.glob(f'sep/*.pdf')

    merge = PdfFileMerger()
    for file in pdf_files:
        reader = PdfFileReader(open(file, 'rb'))
        with open(file, 'rb') as f:
            text = extract_text(f)
            if 'This page intentionally left blank' not in text:
                merge.append(reader)
        os.remove(f'{file}')
    merge.write('Combined_Without_Blank.pdf')

main()