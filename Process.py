'''
Created on Mar 28, 2018

@author: joe
'''
from math import ceil
from test.test_codecs import CodePageTest
from pip._vendor.distlib.locators import Page
from tkinter import *

class process(object):

    def __init__(self, dataSize, codeSize, processID, frameSize):

        self.dataSIZE = dataSize
        self.dataPageCount = ceil(dataSize / frameSize)
        
        self.codeSIZE = codeSize
        self.codePageCount = ceil(codeSize / frameSize)
        self.PID = processID
        
    
        #maps data and code sections to pages and frames
        self.dataPageTable = {"Page" : [], "Frame" : []}
        self.codePageTable = {"Page" : [], "Frame" : []}
        
        self.dataIndex = 0
        self.codeIndex = 0
        
    def printPageTables(self,display):
        display.insert(INSERT,"\nProcess: "+str(self.PID)+" Page Table\n")
        display.insert(INSERT,("TYPE:\tPAGE:\tFRAME")+"\n")
        for i in self.dataPageTable["Page"]:
            display.insert(INSERT,("data\t"+str(i)+"\t"+str(self.dataPageTable["Frame"][i])+"\n"))
        for i in self.codePageTable["Page"]:
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
        self.dataPageTable["Page"].append(page)
        self.dataPageTable["Frame"].append(frame)
        self.dataIndex=self.dataIndex+1
    
    def addCodeLink(self,page,frame):
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