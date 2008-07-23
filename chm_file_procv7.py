import chm.chmlib as chmlib
import chm.extra as extra
import chm.chm as chm
import os
import sys
import re
import urllib
import urlgrabber
from BeautifulSoup import BeautifulSoup

chmDir='/home/rexa/Desktop/books/Python/'
#chmDir='/home/rexa/Desktop/books/hardcases/'
tempPath='/home/rexa/tempCHM/'
res=os.listdir(chmDir)
res.sort()
resCHM=[resFile for resFile in res if re.search(r'\.chm$',resFile)]

for chmFile in resCHM:
    chmFilePath=chmDir+chmFile

    test=chm.CHMFile()
    test.LoadCHM(chmFilePath)
    searchRes=test.Search('ISBN')
    
    if os.path.exists(tempPath):
        os.system('rm -r \''+tempPath+'\'')
        
    archmageCmdStr='archmage \''+chmFilePath+'\''+' \''+tempPath+'\''
    try:
        retVal=os.system(archmageCmdStr)
    except Exception,e:
        print e

    if retVal:
        print 'Archmage could not extract '+chmFile+', continuing from next loop iteration'
        nameStr='touch \''+chmFilePath+'!!!_ArchiveExtractFail\''
        os.system(nameStr)        
        continue #skip this file

    #mainPageFile=searchRes[1]['Main Page']
    if (not searchRes[0]):
        print 'pychm searched for ISBN: searchRes empty for '+chmFile+', continuing to next loop iteration'
        nameStr='touch \''+chmFilePath+'!!!_ISBNSearchFail\''
        os.system(nameStr)
        continue
    
    try:
        mainPageFile=searchRes[1].items()[0][1]
        mainPagePath=tempPath+mainPageFile
        page=urlgrabber.urlopen(mainPagePath)
    except Exception,e:
        mainPageFile=searchRes[1].items()[0][1]
        mainPageFile=mainPageFile.lower()
        mainPagePath=tempPath+mainPageFile
        page=urlgrabber.urlopen(mainPagePath)

    soup = BeautifulSoup(page)
    
    resSoup=soup.body.find(text=re.compile(r'ISBN'))
    
    #here, check to see how many characters come after 'ISBN'
    #if the number is more than 8, we likely are given the ISBN number in
    #resSoup.string, and so we should grab it
    ISBNStart=resSoup.string.find('ISBN')
    ISBNEnd=ISBNStart+len('ISBN')
    charsAfterISBN=len(resSoup.string)-(ISBNEnd+1)
    
    if (charsAfterISBN > 8):
        ISBNNum=resSoup.string[ISBNEnd:]
    else:
        try:
            ISBNNum=resSoup.next.next.contents[0]
        except Exception,e:
            ISBNNum=resSoup.next.contents[0]
    
    ISBNNum=ISBNNum.lstrip(':').strip()
    os.system('rm -r \''+tempPath+'\'')
    
    nameStr='touch \''+chmFilePath+'___'+ISBNNum+'\''
    os.system(nameStr)
    
    #test.GetArchiveInfo()
    #test.GetIndex()
    #ttree=test.GetTopicsTree()
    
    #treeSoup=BeautifulSoup(ttree)
    #treeInfo=test.GetWindowsInfo()
    #test.title