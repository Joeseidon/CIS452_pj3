'''
Created on Mar 28, 2018

@author: joe
'''
from math import ceil
from test.test_codecs import CodePageTest
from pip._vendor.distlib.locators import Page
from tkinter import *

class process(object):
    '''
    classdocs
    '''
    
    
    
    
    def __init__(self, dataSize, codeSize, processID, frameSize):
        '''
        Constructor
        '''
        self.dataSIZE = dataSize
        self.dataPageCount = ceil(dataSize / frameSize)
        
        self.codeSIZE = codeSize
        self.codePageCount = ceil(codeSize / frameSize)
        self.PID = processID
        
        #print("PID: "+str(self.PID)+" "+str(self.dataPageCount)+" "+str(self.codePageCount))
    
        #maps data and code sections to pages and frames
        self.dataPageTable = {"Page" : [], "Frame" : []}
        self.codePageTable = {"Page" : [], "Frame" : []}
        
        self.dataIndex = 0
        self.codeIndex = 0
        
    def printPageTables(self,display):
        #print("Process: "+str(self.PID))
        #print("TYPE:\tPAGE:\tFRAME")
        display.insert(INSERT,"Process: "+str(self.PID)+"\n")
        display.insert(INSERT,("TYPE:\tPAGE:\tFRAME")+"\n")
        for i in self.dataPageTable["Page"]:
            #print("data\t"+str(i)+"\t"+str(self.dataPageTable["Frame"][i]))
            display.insert(INSERT,("data\t"+str(i)+"\t"+str(self.dataPageTable["Frame"][i])+"\n"))
        for i in self.codePageTable["Page"]:
            #print("code\t"+str(i)+"\t"+str(self.codePageTable["Frame"][i]))
            display.insert(INSERT,("code\t"+str(i)+"\t"+str(self.codePageTable["Frame"][i])+"\n"))
        
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