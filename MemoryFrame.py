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
    
    content = 'Frame'
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
        
        