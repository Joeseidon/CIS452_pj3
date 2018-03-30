'''
Created on Mar 28, 2018

@author: joe
'''
from math import ceil
from test.test_codecs import CodePageTest
from pip._vendor.distlib.locators import Page

class process(object):
    '''
    classdocs
    '''
    
    #maps data and code sections to pages and frames
    dataPageTable = {"Page" : [], "Frame" : []}
    codePageTable = {"Page" : [], "Frame" : []}
    
    dataIndex = 0
    codeIndex = 0
    
    codePageCount = 0
    dataPageCount = 0
    
    
    def __init__(self, dataSize, codeSize, processID, frameSize):
        '''
        Constructor
        '''
        self.dataSIZE = dataSize
        self.dataPageCount = ceil(dataSize / frameSize)
        
        self.codeSIZE = codeSize
        self.codePageCount = ceil(codeSize / frameSize)
        self.PID = processID
        
        print("PID: "+str(self.PID)+" "+str(self.dataPageCount)+" "+str(self.codePageCount))
        
    def processData(self,dataSIZE,codeSIZE):
        print("Proces: "+str(self.PID)+ " Loaded into RAM\n")
        print("\tData Size: "+str(dataSIZE)+"\n")
        print(self.dataPageTable)
        print("\n\tCode Size: "+str(codeSIZE)+"\n")
        print(self.codePageTable)
        print("\n")
    
    def getPID(self):
        return self.PID
    def addDataLink(self,page,frame):
        print("add P:"+str(page)+ " F:"+str(frame))
        self.dataPageTable["Page"].append(page)
        self.dataPageTable["Frame"].append(frame)
        self.dataIndex=self.dataIndex+1
    
    def addCodeLink(self,page,frame):
        print("add P:"+str(page)+ " F:"+str(frame))
        self.codePageTable["Page"].append(page)
        self.codePageTable["Frame"].append(frame)
        self.codeIndex=self.dataIndex+1
    
    def getCodePageTable(self):
        return self.codePageTable
    def getDataPageTable(self):
        return self.dataPageTable
    def getCodeSize(self):
        return self.codeSIZE
    def getDataSize(self):
        return self.dataSIZE
    def getCodePageCount(self):
        return self.codePageCount
    def getDataPageCount(self):
        return self.dataPageCount