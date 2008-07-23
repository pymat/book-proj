from pyPdf import PdfFileWriter, PdfFileReader
#alternately use pdftk in.pdf 2-end cat output out.pdf

output = PdfFileWriter()
input1 = PdfFileReader(file("/home/rexa/Desktop/books/look_into/Beginning Algorithims (2006).pdf", "rb"))

print input1.getNumPages()

for i in range(1,input1.getNumPages()):
    output.addPage(input1.pages[i])
    

# finally, write "output" to document-output.pdf
outputStream = file("/home/rexa/Desktop/document-output.pdf", "wb")
output.write(outputStream)
outputStream.close()