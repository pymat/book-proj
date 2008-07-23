from pyPdf import PdfFileWriter, PdfFileReader
import pyPdf
import os
import re

basePath='/home/rexa/python/Python/'
fileList=os.listdir(basePath)
fileList.sort()

for file in fileList:
    rePDF=re.compile(r'\.pdf')
    reCHM=re.compile(r'\.chm')
    
    if rePDF.search(file):
        filePath=basePath+file
        fileHandle=open(filePath,'rb')
        inputPDF = PdfFileReader(fileHandle)
        pdfPage1=inputPDF.getPage(0)
        page1Text=pdfPage1.extractText()
        
        pdfPage2=inputPDF.getPage(1)
        page2Text=pdfPage2.extractText()        
        
        print "title = %s" % (inputPDF.getDocumentInfo().title)

