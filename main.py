from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
import glob
from pdfminer.high_level import extract_text
import os 
# import pandas as pd

def main():
    separate_ballots = 'SeparateBallots'
    if not os.path.exists(separate_ballots):
        os.makedirs(separate_ballots)
        print('Place ballots in SerparateBallots folder')
        return 0
    

    sep = 'sep'
    if not os.path.exists(sep):
        os.makedirs(sep)
    
    pdf_files = glob.glob(f'SeparateBallots/*.pdf')
    # df = pd.DataFrame(data={})
    
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
        os.remove(file)
    os.removedirs(sep)
    if os.path.exists('CombinedBallots_WoutBlank.pdf'):
        os.remove('CombinedBallots_WoutBlank.pdf')
    merge.write('CombinedBallots_WoutBlank.pdf')

main()