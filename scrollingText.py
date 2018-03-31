'''
Created on Mar 31, 2018

@author: joe
'''
import tkinter as tki
class TextObj(tki.Frame):
    '''
    classdocs
    '''


    def __init__(self, master):
        '''
        Constructor
        '''
        tki.Frame.__init__(self,master, width=600, height=600)
        self.pack(fill="both", expand=True)
        # ensure a consistent GUI size
        self.grid_propagate(False)
        # implement stretchability
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.txt = tki.Text(self, borderwidth=3, relief="sunken")
        self.txt.config(font=("consolas", 12), undo=True, wrap='word')
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        
        scrollb = tki.Scrollbar(self, command=self.txt.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set
        
    def insert(self,updateMethod,text):
        self.txt.insert(updateMethod,text)