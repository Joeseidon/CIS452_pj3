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
            
    def loadTable(self,frame,pid,segment,pagenum):
        self.frame_Table['PID'].append(pid)
        self.frame_Table['frameID'].append(frame)
        self.frame_Table['Segment'].append(segment)
        self.frame_Table['PageNum'].append(pagenum)
            
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
    
    def printMemoryTable(self):
        x = 0
        print("Physical Memory <-> Frame Table")
        print("FRAME:\tPID:\tTYPE:\tPAGE:")
        for i in self.frame_Table["frameID"]:
            if len(self.frame_Table["PID"]) <= x :
                print(str(i) + "\t--\t--\t--")
            else:
                print(str(i) + "\t" + str(self.frame_Table["PID"][x]) + "\t" + str(self.frame_Table["Segment"][x]) + "\t" + str(self.frame_Table["PageNum"][x]))
                x=x+1
      
    def removeProcess(self, PID):
        #if process cannot be removed, set to false
        status = True
        
        #for i in self.frame_Table['PID']:
        l = len(self.frame_Table['PID'])
        for i in range(l-1,-1,-1):
            print('comparing: i=' + str(self.frame_Table['PID'][i])+" to pid="+str(PID) + " len="+str(len(self.frame_Table['PID'])))
            if self.frame_Table['PID'][i] == PID:
                del self.frame_Table['PID'][i]
                self.frame_list[self.frame_Table['frameID'][i]].freeFrame()
                del self.frame_Table['frameID'][i]
                del self.frame_Table['Segment'][i]
                del self.frame_Table['PageNum'][i]
                
        
        
        return status