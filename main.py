from PyPDF2 import PdfFileMerger, PdfFileReader
import glob

def main():
    merger = PdfFileMerger()
    url = "SeparateBallots/"
    pdf_files = glob.glob(f'{url}*.pdf')
    
    for file in pdf_files:
        merger.append(PdfFileReader(open(file, 'rb')))
    
    merger.write('Combined.pdf')

main()