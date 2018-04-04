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
    
    frame_Table = {"frameID" : [],
                   "PID" : [],
                   "Segment" : [],
                   "PageNum" : []
                   }
    
    
    def __init__(self, master, numFrames, FrameSize):
        '''
        Constructor
        '''
        LabelFrame.__init__(self,master, bd=4)
        #self.grid()
        self.createFrames(numFrames, FrameSize)
        
        
        self.pack(fill="both", expand="yes")
    
    def createFrames(self, numFrames, FrameSize): 
        for i in range(numFrames):
            self.frame_list.append(MemFrame(self, FrameSize, i))
            self.frame_Table['frameID'].append(i)
            #create table
            self.frame_Table['PID'].append(None)
            self.frame_Table['Segment'].append(None)
            self.frame_Table['PageNum'].append(None)
            
    def loadTable(self,frame,pid,segment,pagenum):
        for x in self.frame_Table["frameID"]:
            if x == frame:  
                self.frame_Table['PID'][x]=pid
                #self.frame_Table['frameID'].append(frame)
                self.frame_Table['Segment'][x] = segment
                self.frame_Table['PageNum'][x] = pagenum
                break;
            
    def loadProcess(self, executable):
        #if process cannot be added, set to false
        pstatus = False
        cstatus = False
        
        ccount = executable.getCodePageCount()
        dcount = executable.getDataPageCount()
        for i in range(ccount):
            for x in self.frame_list:
                if(x.isFree()):
                    executable.addCodeLink(i,x.frameID)
                    pstatus = True
                    x.loadPage(executable.getPID(),'CODE',i)
                    self.loadTable(x.getFrameID(),executable.getPID(),'CODE',i)
                    break #frame found
        for i in range(dcount):
            for x in self.frame_list:
                if(x.isFree()):
                    executable.addDataLink(i,x.frameID)
                    cstatus = True
                    x.loadPage(executable.getPID(),'DATA',i)
                    self.loadTable(x.getFrameID(),executable.getPID(),'DATA',i)
                    break #frame found
        
        return pstatus & cstatus
    
    def printMemoryTable(self,display):
        display.insert(INSERT,"\nPhysical Memory <-> Frame Table"+"\n")
        display.insert(INSERT,"FRAME:\tPID:\tTYPE:\tPAGE:"+"\n")

        for i in self.frame_Table["frameID"]:
            if self.frame_Table["PID"][i] == None :
                display.insert(INSERT,(str(i) + "\t--\t--\t--")+"\n")
            else:
                display.insert(INSERT,(str(i) + "\t" + str(self.frame_Table["PID"][i]) + "\t" + str(self.frame_Table["Segment"][i]) + "\t" + str(self.frame_Table["PageNum"][i])+"\n"))
      
    def removeProcess(self, PID):
        #if process cannot be removed, set to false
        status = True
        
        l = len(self.frame_Table['PID'])
        for i in range(l-1,-1,-1):
            if self.frame_Table['PID'][i] == PID:
                self.frame_Table['PID'][i]= None
                self.frame_list[self.frame_Table['frameID'][i]].freeFrame()
                #del self.frame_Table['frameID'][i]
                self.frame_Table['Segment'][i] = None
                self.frame_Table['PageNum'][i] = None
        
        return status