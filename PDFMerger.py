import PyPDF2

pdf1 = input("Enter file1 Location and Location and name: ")
pdf2 = input("Enter file2 Location and Location and name: ")
pdfiles = [pdf1, pdf2]

#pdfiles = ["I1.pdf", "I2.pdf","I3.pdf"]
merger = PyPDF2.PdfMerger()

for filename in pdfiles:
    pdfFile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()

merger.write('Im.pdf')
