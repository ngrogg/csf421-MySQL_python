#!/usr/bin/python2.7

import mysql.connector
import tkMessageBox
from Tkinter import *
# Fuck it, import everything!

class Application(Frame):

    # When go back button is hit on query screen
    def back_query(self):
        self.button1.pack_forget()
        self.createWidgets()

    # When go back button is hit on insertion screen
    def back_insertion(self):
        self.buttona.pack_forget()
        self.createWidgets()

    # Button to run query
    def query(self):
        # Insert title text
        self.Title = 
        # Remove other buttons

        self.INSERTION.pack_forget()
        self.QUIT.pack_forget()
        self.QUERY.pack_forget()

        # create Go Back button
        self.button1 = Button(self)
        self.button1["text"] = "Back"
        self.button1["command"] = self.back_query
        self.button1.pack({"side" : "left"})


    # Button to insert data
    def insertion(self):
        self.INSERTION.pack_forget()
        self.QUIT.pack_forget()
        self.QUERY.pack_forget()

        # Create Go Back button
        self.buttona = Button(self)
        self.buttona["text"] = "Back"
        self.buttona["command"] = self.back_insertion
        self.buttona.pack({"side" : "left"})

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
