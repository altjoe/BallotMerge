from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
from pdfminer.high_level import extract_text
import glob
import os

def main():
    separate_ballots = 'SeparateBallots'
    if not os.path.exists(separate_ballots):
        os.makedirs(separate_ballots)
        print('Place ballots in SerparateBallots folder')
        return 0
    
    pdf_files = glob.glob(f'SeparateBallots/*.pdf')


    writer = PdfFileWriter()
    files = []
    for filename in pdf_files:
        file = open(filename, 'rb')
        if 'This page intentionally left blank' in extract_text(file):
            reader = PdfFileReader(file)
            for page_num in range(reader.numPages - 1):
                writer.add_page(reader.getPage(page_num))
        else:
            reader = PdfFileReader(file)
            for page_num in range(reader.numPages):
                writer.add_page(reader.getPage(page_num))
                files.append(file)

    with open('CombinedBallots_WoutBlank.pdf', 'wb') as f:
        writer.write(f)
    
    for file in files:
        file.close()

main()