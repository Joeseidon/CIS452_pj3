'''
Created on Mar 27, 2018

@author: joe
'''
from tkinter import *
from Memory import RAM
from Process import process
from asyncio.tasks import wait
from scrollingText import TextObj


root = Tk()
#outputText = Text(root,relief="sunken")
#inputText = Text(root,relief="sunken")

inputText = TextObj(root)
outputText = TextObj(root)

ram = RAM(root,8,512)

cmdCount = 0
index = 0
processQueue = []

def processCMD(cmdStr):
    words = cmdStr.split(" ") 
    
    if words[1] == '-1\n' or words[1] == '-1':
        output = 'PID: ' + words[0] + ' Terminates\n'
        intext = words[0] + " " + words[1] + "\n"
        
        inputText.insert(INSERT,intext)
        outputText.insert(INSERT,output)       
        #remove process = PID from process queue and reallocate memory
        ram.removeProcess(int(words[0]))
    else:
        intext = words[0] + " " + words[1] + " " + words[2] + "\n"
        output = 'PID: ' + words[0] + ' arrives: '+'\tCode/Text: ' + words[1] + '\tData: ' + words[2]
        
        inputText.insert(INSERT,intext)
        outputText.insert(INSERT,output)
        
        PID = int(words[0])
        dataSIZE = int(words[2])
        codeSIZE = int(words[1])
        
        x = process(dataSIZE,codeSIZE,PID,500)
        
        processQueue.append(x)
        
        x.printPageTables(display=outputText)
        
        #Allocate Memory
        if ram.loadProcess(x):
            #x.processData(dataSIZE,codeSIZE)
            x.printPageTables(display=outputText)
        else:
            print("Load Failed")
            #x.processData(dataSIZE,codeSIZE)
            x.printPageTables(display=outputText)
        
    ram.printMemoryTable(display=outputText)
        
        
    
    
def nextCMD():
    global index
    if index < cmdCount:
        processCMD(inputCMDs[index])
        index = index + 1

if __name__ == '__main__':
    
    inputCMDs=[]
    stepIndex = 0
    #read file 
    with open("testfile.txt", "r") as file:
        inputCMDs=(file.readlines())
        cmdCount = len(inputCMDs)
        
    inputText.pack(side=LEFT)
    outputText.pack(side=RIGHT)
    
    button = Button(root, text="Next", command=nextCMD)

    button.pack(side=BOTTOM)
    
    root.mainloop(0)