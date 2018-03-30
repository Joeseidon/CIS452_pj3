'''
Created on Mar 27, 2018

@author: joe
'''
from tkinter import *
from MemoryFrame import MemFrame
from Process import process
class RAM(LabelFrame):
    '''
    classdocs
    '''
    frame_list = []
    
    frame_Table = {"frameID" : [], "PID" : [], "Segment" : [], "PageNum" : []}
    

    def __init__(self, master, numFrames, FrameSize):
        '''
        Constructor
        '''
        Frame.__init__(self,master, bd=4)
        self.grid()
        self.createFrames(numFrames, FrameSize)
        
        self.pack(fill="both", expand="yes")
    
    def createFrames(self, numFrames, FrameSize): 
        for i in range(numFrames):
            self.frame_list.append(MemFrame(self, FrameSize, i))
            
    def loadProcess(self, executable):
        #if process cannot be added, set to false
        pstatus = False
        cstatus = False
        
        ccount = executable.getCodePageCount()
        dcount = executable.getDataPageCount()
        print("dcount: "+str(dcount)+" ccount:"+str(ccount))
        for i in range(ccount):
            for x in self.frame_list:
                if(x.isFree()):
                    executable.addCodeLink(i,x.frameID)
                    pstatus = True
                    x.loadPage(executable.getPID(),'CODE',i)
                    break #frame found
        for i in range(dcount):
            for x in self.frame_list:
                if(x.isFree()):
                    executable.addDataLink(i,x.frameID)
                    cstatus = True
                    x.loadPage(executable.getPID(),'DATA',i)
                    break #frame found
        
        return pstatus & cstatus
        
    def removeProcess(self, PID):
        #if process cannot be removed, set to false
        status = True
        
        
        return status