import os,re,sys,time


paperDir='/home/rexa/Desktop/papers/'
paperList=os.listdir(paperDir)
for paper in paperList:
    pdfCmdStr="pdftotext -f 1 -l 1 "+paperDir+re.escape(paper)+" -"
    fd=os.popen(pdfCmdStr)
    pdfLines=fd.readlines()
    
    if len(pdfLines[0])>1 \
       and len(pdfLines[0])<50 \
       and (pdfLines[0].find('ISSN')==-1):
        print len(pdfLines[0])," - ",pdfLines[0].title()
        time.sleep(.3)
    