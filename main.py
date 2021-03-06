'''
Created on Mar 27, 2018

@author: joe
'''
import tkinter as tk
from Memory import RAM
from Process import process
from scrollingText import TextObj

#Main window
root = tk.Tk()

#Scrolling text frames
inputText = TextObj(root)
outputText = TextObj(root)

#Simulated RAM
ram = RAM(root,8,512)

#Global variables 
cmdCount = 0
index = 0

def processCMD(cmdStr):
    #Split command string into components
    words = cmdStr.split(" ") 
    
    #Print line for user friendly output
    outputText.insert(tk.INSERT,"======================================================\n")
    
    #Process Termination Sequence
    if words[1] == '-1\n' or words[1] == '-1':
        #Print input commands
        output = 'PID: ' + words[0] + ' Terminates\n'
        intext = words[0] + " " + words[1]
        
        inputText.insert(tk.INSERT,intext)
        outputText.insert(tk.INSERT,output) 
              
        #Remove process = PID from process queue and reallocate memory
        ram.removeProcess(int(words[0]))
    else: #Process Loading Sequence
        #Print out cmd string components
        intext = words[0] + " " + words[1] + " " + words[2]
        output = 'PID: ' + words[0] + ' arrives: '+'\tCode/Text: ' + words[1] + '\tData: ' + words[2]
        
        inputText.insert(tk.INSERT,intext)
        outputText.insert(tk.INSERT,output)
        
        #Convert input string into usable int values
        PID = int(words[0])
        dataSIZE = int(words[2])
        codeSIZE = int(words[1])
        
        #Create Processes
        x = process(dataSIZE,codeSIZE,PID,512)
        
        #Allocate Memory
        if ram.loadProcess(x):
            x.printPageTables(display=outputText)
        else:
            print("Load Failed")
            x.printPageTables(display=outputText)
        
    ram.printMemoryTable(display=outputText)
    
    outputText.insert(tk.INSERT,"\n\n")    
        
#This method is linked to the next button on the main window
#and controls the operation of this program.   
def nextCMD():
    global index
    if index < cmdCount:
        processCMD(inputCMDs[index])
        index = index + 1

if __name__ == '__main__':
    #Process variables 
    inputCMDs=[]
    
    #Read commands from file
    with open("testfile.txt", "r") as file:
        inputCMDs=(file.readlines())
        cmdCount = len(inputCMDs)
    
    #Insert text frames into main window
    inputText.pack(side=tk.LEFT)
    outputText.pack(side=tk.RIGHT)
    
    #Add button to main window
    button = tk.Button(root, text="Next", command=nextCMD)
    button.pack(side=tk.BOTTOM)
    
    #Application Loop
    root.mainloop(0)