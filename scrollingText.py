'''
Created on Mar 31, 2018

@author: joe
'''
import tkinter as tki
class TextObj(tki.Frame):
 
    def __init__(self, master):
        tki.Frame.__init__(self,master, width=600, height=600)
        self.pack(fill="both", expand=True)

        self.grid_propagate(False)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        #Text Field
        self.txt = tki.Text(self, borderwidth=3, relief="sunken")
        self.txt.config(font=("consolas", 12), undo=True, wrap='word')
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        
        #Implement scroll bar
        scrollb = tki.Scrollbar(self, command=self.txt.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set
        
    #Place Text in Text Field    
    def insert(self,updateMethod,text):
        self.txt.insert(updateMethod,text)
        self.txt.see("end")