#!/usr/bin/python2.7

import mysql.connector
#import Tkinter
import tkMessageBox

from Tkinter import *

class Application(Frame):

    # Button to run query
    def query(self):
        print "test for now"
        
    # Button to insert data
    def insertion(self):
        print "test for now"

    def createWidgets(self):
        # Button Parameters
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        # Create Button
        self.QUIT.pack({"side": "left"})

        # Button parameters for Query button
        self.QUERY = Button(self)
        self.QUERY["text"] = "Query",
        self.QUERY["command"] = self.query

        # Add Query Button to GUI
        self.QUERY.pack({"side": "left"})

        # Button Parameters for Insertion button
        self.INSERTION = Button(self)
        self.INSERTION["text"] = "Insertion",
        self.INSERTION["command"] = self.insertion

        # Create Button
        self.INSERTION.pack({"side": "left"})


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
