#!/usr/bin/python2.7

import mysql.connector
import tkMessageBox
from Tkinter import *
# Fuck it, import everything!

class Application(Frame):

    # When go back button is hit on query screen
    def back_query(self):
        # Remove created buttons
        self.buttona.pack_forget()

        # Create Home buttons
        self.createWidgets()

    # When go back button is hit on insertion screen
    def back_insertion(self):
        # Remove created buttons
        self.buttonb.pack_forget()
       
        # Create Home buttons
        self.createWidgets()

    # When go back button is hit on removal screen
    def back_removal(self):
        # Remove created buttons
        self.buttonc.pack_forget()

        # Create Home buttons
        self.createWidgets()

    # When go back button is hit on export table screen
    def back_exportTable(self):
        # Remove created buttons
        self.buttond.pack_forget()

        # Create Home buttons
        self.createWidgets()

    # When go back button is hit on export query screen
    def back_exportQuery(self):
        # Remove created buttons
        self.buttone.pack_forget()

        # Create Home buttons
        self.createWidgets()

    # Button to run query
    def query(self):
       # Insert title text

        # Remove other buttons
        self.INSERTION.pack_forget()
        self.QUIT.pack_forget()
        self.QUERY.pack_forget()
        self.REMOVAL.pack_forget()
        self.EXPORTQUERY.pack_forget()
        self.EXPORTTABLE.pack_forget()

        # create Go Back button
        self.buttona = Button(self)
        self.buttona["text"] = "Back"
        self.buttona["command"] = self.back_query
        self.buttona.pack({"side" : "left"})


    # Button to insert data
    def insertion(self):
        # Insert title text

        # Remove other buttons
        self.INSERTION.pack_forget()
        self.QUIT.pack_forget()
        self.QUERY.pack_forget()
        self.REMOVAL.pack_forget()
        self.EXPORTQUERY.pack_forget()
        self.EXPORTTABLE.pack_forget()

        # Create Go Back button
        self.buttonb = Button(self)
        self.buttonb["text"] = "Back"
        self.buttonb["command"] = self.back_insertion
        self.buttonb.pack({"side" : "left"})

    # Button to remove data
    def removal(self):
        # Insert title text

        # Remove Home buttons
        self.INSERTION.pack_forget()
        self.QUIT.pack_forget()
        self.QUERY.pack_forget()
        self.REMOVAL.pack_forget()
        self.EXPORTQUERY.pack_forget()
        self.EXPORTTABLE.pack_forget()

        # Create Go Back button
        self.buttonc = Button(self)
        self.buttonc["text"] = "Back"
        self.buttonc["command"] = self.back_removal
        self.buttonc.pack({"side" : "left"})


    # Button to export table
    def exportTable(self):
        # Insert title text

        # Remove Home buttons
        self.INSERTION.pack_forget()
        self.QUIT.pack_forget()
        self.QUERY.pack_forget()
        self.REMOVAL.pack_forget()
        self.EXPORTQUERY.pack_forget()
        self.EXPORTTABLE.pack_forget()

        # Create Go Back button
        self.buttond = Button(self)
        self.buttond["text"] = "Back"
        self.buttond["command"] = self.back_exportTable
        self.buttond.pack({"side" : "left"})

    # Button to export query
    def exportQuery(self):
        # Insert title text

        # Remove Home buttons
        self.INSERTION.pack_forget()
        self.QUIT.pack_forget()
        self.QUERY.pack_forget()
        self.REMOVAL.pack_forget()
        self.EXPORTQUERY.pack_forget()
        self.EXPORTTABLE.pack_forget()

        # Create Go Back button
        self.buttone = Button(self)
        self.buttone["text"] = "Back"
        self.buttone["command"] = self.back_exportQuery
        self.buttone.pack({"side" : "left"})

    # Home page 
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
        self.QUERY["text"] = "Query"
        self.QUERY["command"] = self.query

        # Add Query Button to GUI
        self.QUERY.pack({"side": "left"})

        # Button Parameters for Insertion button
        self.INSERTION = Button(self)
        self.INSERTION["text"] = "Insertion"
        self.INSERTION["command"] = self.insertion

        # Create Button
        self.INSERTION.pack({"side": "left"})

        # Button for Removal
        self.REMOVAL = Button(self)
        self.REMOVAL["text"] = "Removal"
        self.REMOVAL["command"] = self.removal
        self.REMOVAL.pack({"side": "left"})

        # Button for Exporting table
        self.EXPORTTABLE = Button(self)
        self.EXPORTTABLE["text"] = "ExportTable"
        self.EXPORTTABLE["command"] = self.exportTable
        self.EXPORTTABLE.pack({"side": "left"})

        # Button for Exporting Query
        self.EXPORTQUERY = Button(self)
        self.EXPORTQUERY["text"] = "ExportQuery"
        self.EXPORTQUERY["command"] = self.exportQuery
        self.EXPORTQUERY.pack({"side":"left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
