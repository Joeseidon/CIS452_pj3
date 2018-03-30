'''
Created on Mar 27, 2018

@author: joe
'''
from tkinter import *
from pip._vendor.distlib.locators import Page
class MemFrame(Label):
    '''
    classdocs
    '''

    MaxSize = 0
    
    frameID = 0
    
    free = True
    
    content = 'Free'
    PID = 0
    pageType = ""
    page = 0
    
    def __init__(self, master, frameSize, frameId):
        '''
        Constructor
        '''
        Label.__init__(self, master, height=5,width=25,bd=5, text=self.content, relief=RAISED)
        
        self.MaxSize = frameSize
        self.frameID = frameId
        
        
        print('Frame Created'+str(self.frameID))
        
        self.pack(side=RIGHT)
        
    def isFree(self):
        return self.free
    
    def loadPage(self,PID,pageType,page):
        self.free = False
        self.PID = PID
        self.pageType = pageType
        self.page = page
        if pageType == "CODE":
            t = "Code-"+str(page)+ " of P" + str(PID)
            self.config(text = t)
            self.update_idletasks()
        else:
            t = "Data-"+str(page)+ " of P" + str(PID)
            self.config(text = t)
            self.update_idletasks()
            
    def freeFrame(self):
        self.free = True
        self.PID = 737
        self.pageType = ""
        self.page = 0
        self.config(text="Free")
        self.update_idletasks()
        
    def getFrameID(self):
        return self.frameID
        